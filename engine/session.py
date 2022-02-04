from flask import session,g,redirect,url_for
from engine import init
import functools

def load_current_user():
    token=session.get("token")
    if token is None:
        g.token=None
    else:
        g.token=token

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.token is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

def asDict(row):
    dict = {column: str(getattr(row, column)) for column in row.__table__.c.keys()}
    return dict
