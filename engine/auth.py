from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash
from sqlalchemy import text
from engine import sessionLocal
from engine.build import init
from engine.database import sessionLocal
from werkzeug.exceptions import abort
import datetime
import functools
import routes
import uuid
import configparser
import sys

apps=init()
bp=Blueprint('auth',__name__)
conf=configparser.ConfigParser()
conf.read('config/App.ini')

def makesure(req):
    query=text("SELECT * FROM %s WHERE %s='%s'"%(conf['Auth']['Table'],conf['Auth']['IdentityColumn'],req['un']))
    res=sessionLocal.execute(query).scalar()
    if res is not None:
        return True
    return res

@bp.route("/login", methods=("GET", "POST"))
def login():
    # create sample login
    if request.method=='POST':
        authReq={
            'un':request.form['username'],
            'pass':request.form['password']
        }
        if makesure(authReq) is None:
            print(makesure(authReq))
        else:
            session.clear()
            session['user_id']=authReq['un']
            return redirect(url_for('route.index'))
    return render_template("auth.jinja")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    print(user_id)
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
