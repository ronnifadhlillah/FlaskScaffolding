from flask import g,Blueprint,render_template,session
from engine import sessionLocal
from engine.build import init
from engine.auth import login_required
from apps.sample_model import MockData
from werkzeug.exceptions import abort
from sqlalchemy import desc,asc
import datetime
import json
import functools

apps=init()
bp=Blueprint('route',"FLASK SCAFFOLDING")

@bp.route('/')
@login_required
def index():
    # Write down query and route to page
    return render_template('index.html')

@bp.route('/home')
def home():
    return render_template('home.html')
