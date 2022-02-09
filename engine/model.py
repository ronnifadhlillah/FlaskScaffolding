from sqlalchemy.ext.declarative import DeclarativeMeta,declarative_base
from flask import request
from datetime import datetime
from engine import init
import json
import bcrypt
import time
import random
import string

# initialize engine module in model
a=init()

# Like mixer this file is contain everything that you want to write.
# This code below is a stimulous of JSON encoder if you see an error JSON seriazible.
class encoder(json.JSONEncoder):
    def encoder_p_0(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

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
