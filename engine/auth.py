from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash
from engine import sessionLocal
from engine.build import init
from engine.database import sessionLocal
from werkzeug.exceptions import abort
import datetime
import functools
import routes
import uuid

apps=init()
bp=Blueprint('auth',__name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['user_id'] is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

def makesure(req):
    query=sessionLocal.text("SELECT * FROM %s WHERE %s=%s AND %s=%s"%())
    if query is not None:
        # buildSession
        pass
    return False

def session():
    pass

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        print(g.user)
        g.user = None

@bp.route("/login", methods=("GET", "POST"))
def login():
    # create sample login
    if request.method=='POST':
        authReq={
            'un': request.form['username']
        }
        error=None
        if error is None:
            session.clear()
            session['user_id']=authReq['un']
            session['session']=uuid.uuid4()
            return redirect(url_for('route.index'))
    return render_template("auth.jinja")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
