from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash
from sqlalchemy import text,inspect
from engine import init,sessionLocal,check_hash
from engine.model import encoder
from werkzeug.exceptions import abort
from apps.users_model import Users
import datetime
import functools
import routes
import bcrypt
import configparser
import sys
import uuid

# this file is used to handling login session by default.

apps=init()
bp=Blueprint('auth',__name__)
conf=configparser.ConfigParser()
conf.read('config/app.py')

def makesure(req):
    q=sessionLocal.query(Users).filter_by(username=req['un'])
    sql=q.first()
    # Role Middleware if available
    if sql is not None and check_hash(req['pass'],sql.password) is not False:
        session['token']=uuid.uuid4()
        session['logged_in']=True
        sql2=q.all()
        row = sql2[0]
        row_as_dict = {column: str(getattr(row, column)) for column in row.__table__.c.keys()}
        # print(len(row_as_dict))
        for data in row_as_dict:
            session[data]=row_as_dict[data]
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
    token=session.get("token")
    username=session.get('username')
    if token is None:
        g.token = None
    else:
        g.token=token
        g.username=username

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
