from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash,make_response
from engine import init,sessionLocal,checkHash,loginRequired,asDict,randStr,generateHash,token,getCookie
from werkzeug.exceptions import abort
# from apps.users_model import Users
from sqlalchemy import text
import datetime
import uuid

# this file is used to handling login session by default.

apps=init()
bp=Blueprint('auth',__name__)

def makesure(req):
    # sql=sessionLocal.query(Users).filter_by(username=req['un'])
    # sql=q.first()
    sql=sessionLocal.execute(text(f"""
    SELECT username,password FROM users WHERE username='{req["un"]}'
    """))
    exec1=sql.fetchall()
    columns=sql.keys()
    # User found and password compare logic.
    if len(exec1)>0 and checkHash(request.form["pass"],exec1[0].password) is not False:
        # Build a session
        session['token']=token()
        session['logged_in']=True
        rad=[dict(zip(columns,row)) for row in sql]
        for data in rad:
            session[data]=rad[data]

        sessionLocal.close()
        return True
    else:
        return None

@bp.route("/login", methods=("GET","POST"))
def login():
    
    # create sample login
    session.clear()

    # # Do authentiation
    if request.method=='POST':
        sql=sessionLocal.execute(text(f"""
        SELECT * FROM users WHERE username='{request.form['username']}'
        """))
        exec1=sql.fetchall()
        columns=sql.keys()
        # User found and password compare logic.
        if len(exec1)>0 and checkHash(request.form["password"],exec1[0].password) ==True:
            sql2=sessionLocal.execute(text(f"""
            SELECT * FROM roles_assign WHERE loginId={exec1[0].id}
            """)).fetchall()
            # Build a session
            session['token']=token()
            session['logged_in']=True
            rad=[dict(zip(columns,row)) for row in exec1]

            for data in rad[0]:
                session[data]=rad[0][data]
            for rolesData in sql2:
                session[rolesData.rolesId]=rolesData.rolesId

            sessionLocal.close()
            return redirect(url_for('route.index'))
        error='Check username and password'

        flash(error) # or return redirect page

    return render_template("auth.jinja")


        # error=None

        # if makesure(authReq) is not None:
        #     authenticate=make_response(redirect(url_for('route.index')))
        #     authenticate.set_cookie('name',token())
        #     return authenticate
        # error='Check username and password'

@bp.route("/logout")
def logout():
    session.clear()
    session.pop('name',None)
    return redirect(url_for("auth.login"))
