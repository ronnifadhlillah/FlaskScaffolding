from sqlalchemy.ext.declarative import DeclarativeMeta,declarative_base
from sqlalchemy.engine import Row
from flask import request
from datetime import datetime,date,timedelta
from engine import init
import json
import bcrypt
import time
import random
import string
import decimal
import numpy as np

# initialize engine module in model
a=init()

# Like mixer this file is contain everything that you want to write.
# This code below is a stimulous of JSON encoder if you see an error JSON seriazible.
class JSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.isoformat()  
    elif isinstance(obj, decimal.Decimal):
      return float(obj)  
    elif isinstance(obj, date):
      return obj.isoformat()  
    elif isinstance(obj, Row):
      return dict(obj)
    elif isinstance(obj, timedelta):
      return str(obj)
    elif isinstance(obj, np.integer):
      return int(obj)
    elif isinstance(obj, np.floating):
      return float(obj)
    elif isinstance(obj, np.ndarray):
      return obj.tolist()
    return super(CustomJSONEncoder, self).default(obj)

def nowInTimestamp():
    cur=datetime.now()
    strftime=cur.strftime('%Y-%m-%d %H:%M:%S')
    epochCon=datetime.timestamp(strftime)
    return epochCon

@a.template_filter('epochConvert')
def timeStampToStr(ts,format='%d/%m/%Y %H:%M:%S'):
    epoch=datetime.datetime.fromtimestamp(int(ts))
    if ts is None:
        return ""
    return epoch.strftime(format)

def generateHash(key):
    salting=bcrypt.gensalt()
    hash=bcrypt.hashpw(key.encode(),salting)
    return hash

def checkHash(key1,key2):
    # compare the string just you've been input
    return bcrypt.checkpw(key1.encode(),key2.encode())

def randStr():
    key = string.ascii_lowercase
    return random.choice(key)

def pageLoadTime():
    # initialize the variable start
    # to store the starting time of
    # execution of program
    start = time.time()

    # take any program but for
    # example we have taken the below
    # program
    a = 0
    for i in range(1000):
        a += (i**100)

    # now initialized the variable
    # end to store the ending time after
    # execution of program
    end = time.time()
    pl=end-start
    return pl

def copyPat():
    apps=init()
    with apps.app_context():
        return request.url
