from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash,make_response
from engine import init,sessionLocal,checkHash,loadCurrentUser,loginRequired,asDict,randStr,generateHash,token,getCookie
from werkzeug.exceptions import abort
from apps.users_model import Users
import datetime
import uuid

# this file is used to handling login session by default.

apps=init()
bp=Blueprint('auth',__name__)

def makesure(req):
    q=sessionLocal.query(Users).filter_by(username=req['un'])
    sql=q.first()
    # User found and password compare logic.
    if sql is not None and checkHash(req['pass'],sql.password) is not False:
        # Build a session
        session['token']=token()
        session['logged_in']=True
        row=q.all()[0]
        rad=asDict(row)
        for data in rad:
            session[data]=rad[data]
        return True
    else:
        return None

@bp.route("/login", methods=("GET","POST"))
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
            res=make_response(redirect(url_for('route.index')))
            res.set_cookie('name',token())
            return res
        error='Check username and password'
        flash(error)
    return render_template("auth.jinja")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
