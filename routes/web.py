from flask import g,Blueprint,render_template,session,request
from engine import sessionLocal
from engine.build import init,copyPat
from engine.auth import login_required
from apps.sample_model import MockData
from werkzeug.exceptions import abort
from sqlalchemy import desc,asc
import datetime
import json
import functools

apps=init()
bp=Blueprint('route',__name__)

@bp.route('/')
@login_required
def index():
    print(copyPat())
    # Write down query and route to page
    return render_template('index.html')

@bp.route('/home')
@login_required
def home():
    print(copyPat())
    return render_template('home.html')
