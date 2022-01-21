from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash
from sqlalchemy import text
from engine import init,sessionLocal,check_hash
from werkzeug.exceptions import abort
import datetime
import functools
import routes
import bcrypt
import configparser
import sys
import uuid

# This file is just for authentication not register handling.
# If you're not use build in authentication, you can comment "@login_required".
# There's maybe have an error if you're not commented.
# Login & logout page maybe un-available. You can built in manually with different name.

apps=init()
bp=Blueprint('auth',__name__)
conf=configparser.ConfigParser()
conf.read('config/App.ini')

def makesure(req):
    sql="""SELECT *
    FROM %s
    WHERE %s='%s'"""
    query=text(sql%(conf['Auth']['Table'],conf['Auth']['IdentityColumn'],req['un']))
    row=sessionLocal.execute(query).fetchone()

    # Role Middleware if available

    if row is not None and check_hash(req['pass'],row['password']) is not False:
        session['token']=uuid.uuid4()
        return True
    else:
        return None

@bp.route("/login", methods=("GET", "POST"))
def login():
    # create sample login
    session.clear()
    if request.method=='POST':
        authReq={
            'un':request.form['username'],
            'pass':request.form['password']
        }
        error=None
        if makesure(authReq) is not None:
            return redirect(url_for('route.index'))
        error='Check username and password'
        flash(error)
    return render_template("auth.jinja")

@bp.before_app_request
def load_logged_in_user():
    token = session.get("token")
    if token is None:
        g.token = None
    else:
        g.token=token

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.token is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view
