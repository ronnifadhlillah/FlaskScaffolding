from sqlalchemy.ext.declarative import DeclarativeMeta,declarative_base
from datetime import datetime
import json

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
