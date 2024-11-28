from flask import session,g,redirect,url_for,request,make_response
from engine import init,generateHash,randStr,sessionLocal
from datetime import datetime,timedelta
from sqlalchemy import text
import functools

def token():
    return generateHash(randStr())

# def loadCurrentUser():
#     token=session.get("token")
#     if token is None:
#         g.token=None
#     else:
#         g.token=token

def sessionLifetime(a):
    session.lifetime=True
    a.permanent_session_lifetime=timedelta(minutes=60)

# SESSION MIDDLEWARE

def loginRequired(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.id is None or bool(session.items())==False:
            session.clear()
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

def roles(perm=None):
    def decorator(view):
        @functools.wraps(view)
        def rolesFunction(**kwargs):
            sql=sessionLocal.execute(text(f"""
            SELECT * FROM roles_assign WHERE loginId={g.id}
            """)).fetchall()
            roles=[]
            for r in sql:
                roles.append(r.rolesId)

            if all(i not in roles for i in perm):
                return 'Error 404',404
            return view(**kwargs)
        return rolesFunction
    return decorator

def asDict(row):
    dict = {column: str(getattr(row, column)) for column in row.__table__.c.keys()}
    return dict

def getCookie():
    head=request.cookies.get('name')
    return head

def getUserAgent():
    ua=request.user_agent
    return ua
