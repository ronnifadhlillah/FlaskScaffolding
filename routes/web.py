from flask import Blueprint,render_template,session
from engine import sessionLocal
from engine.build import init,server
from apps.sample_model import MockData
from werkzeug.exceptions import abort
from sqlalchemy import desc,asc
import datetime
import json
import functools

apps=init()
bp=Blueprint('route',"FLASK SCAFFOLDING")

# @bp.route('/')
# def index():
#     # Write down query and route to page
#     data=sessionLocal.query(MockData).order_by(desc(MockData.id)).limit(100)
#     return render_template('index.html',data=data)

# Uncomment if you want to redirect to login page for first time load.
# By default, it's set to commented.

# =======================Route=======================

@bp.route('/')
def index():
    # Write down query and route to page
    return render_template('index.html')

@bp.route('/login')
def login():
    return render_template('auth.jinja')

@bp.route('/home')
@login_required
def home():
    return render_template('home.html')
