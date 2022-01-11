from sqlalchemy.ext.declarative import DeclarativeMeta,declarative_base
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
import json
import bcrypt

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

# on consideration
def handleHashing(statement,key,compare_key=None):
    if statement is 'generate hashing':
        generate_password_hash(key)
    elif statement is 'hash validation':
        # return check_password_hash(key,compare_key)
        return key,compare_key

# for bycrypt , install bcrypt module by pip install bycrypt
# def goBcrypt(key):
#     k=b'%s'%(key)
#     salting=bcrypt.gensalt()
#     goHash=bcrypt.hashpw(k,salting)
#     return goHash
#
# def checkBcrypt(key):
#     k=b'%s'%(key)
#     if bcrypt.checkpw(key,goBcrypt(key)):
#         return True
#     else:
#         return False
