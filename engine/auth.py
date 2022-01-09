from flask import g,Blueprint,render_template,session,redirect,request,url_for,flash
from engine import sessionLocal
from engine.build import init
from engine.database import sessionLocal
from werkzeug.exceptions import abort
import datetime
import functools
import routes
import uuid
import configparser

apps=init()
bp=Blueprint('auth',__name__)

def makesure(req):
    conf=configparser.ConfigParser()
    conf.read('config/App.ini')

    query="SELECT * FROM %s WHERE %s=%s"%(conf['Auth']['Table'],conf['Auth']['IdentityColumn'],req['un'])
    print(query)
    # if query is not None:
    #     # buildSession
    #     pass
    # return False

@bp.route("/login", methods=("GET", "POST"))
def login():
    # create sample login
    if request.method=='POST':
        authReq={
            'un': request.form['username']
        }
        makesure(authReq)
        error=None
        if error is None:
            session.clear()
            session['user_id']=authReq['un']
            return redirect(url_for('route.index'))
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
    return redirect(url_for("route.index"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view
