from flask import session,g,redirect,url_for,request,make_response
from engine import init,generateHash,randStr
from datetime import datetime,timedelta
import functools

def token():
    return generateHash(randStr())

def loadCurrentUser():
    token=session.get("token")
    if token is None:
        g.token=None
    else:
        g.token=token

def sessionLifetime(a):
    session.lifetime=True
    a.permanent_session_lifetime=timedelta(minutes=60)

def parsingUserSession(a):
    for k,v in session.items():
        a.jinja_env.globals[k]=v

def loginRequired(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.token is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

def asDict(row):
    dict = {column: str(getattr(row, column)) for column in row.__table__.c.keys()}
    return dict

def getCookie():
    head=request.cookies.get('name')
    return head

def getUserAgent():
    ua=request.user_agent
    return ua
