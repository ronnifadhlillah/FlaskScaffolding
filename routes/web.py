from flask import g,Blueprint,render_template,session,request
from engine import sessionLocal,init,copyPat,loginRequired
from apps.sample_model import MockData
from werkzeug.exceptions import abort
from sqlalchemy import desc,asc
import datetime

# If you're not use build in authentication, you can comment "@login_required".
# There's maybe have an error if you're not commented.
# Login & logout page maybe un-available. You can built in manually with different name.

apps=init()
bp=Blueprint('route',__name__)

@bp.route('/')
@loginRequired
def index():
    # print(copyPat())
    # Write down query and route to page
    return render_template('index.jinja')

@bp.route('/home')
@loginRequired
def home():
    # print(copyPat())
    return render_template('home.jinja')
