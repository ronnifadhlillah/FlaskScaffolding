import functools

from flask import g,Blueprint,render_template,session,redirect,request,url_for
from engine import sessionLocal
from engine.build import init
from werkzeug.exceptions import abort
import datetime

apps=init()
bp=Blueprint('auth','FLASK SCAFFOLDING')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None

@bp.route("/login", methods=("GET", "POST"))
def login():
    return render_template("auth.jinja")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
