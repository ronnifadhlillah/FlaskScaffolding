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

    if row is not None and check_hash(req['pass'],row['password']) is not False:
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
            session.clear()
            session['user_id']=authReq['un']
            return redirect(url_for('route.index'))
        error='Check username and password'
        flash(error)
    return render_template("auth.jinja")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user=user_id

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view
