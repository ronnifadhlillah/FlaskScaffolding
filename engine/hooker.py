import flask
import socket
import configparser
import engine
from engine.model import epochConvert,epochConvertAll,pageLoadTime,locale
from engine.session import getCookie

cfg=configparser.ConfigParser()
cfg.read('config/app.py')
a=flask.Flask(__name__)

# Hooker is direct bind without going throught controller.
# you can directly parsing into view by calling it's 'key'

# hook(key, value) --> Sample
# Calling hook in jinja --> {{key}}

def hook(k,v):
    arr={
        'key':k,
        'value':v
    }
    return arr

# a=init()
@a.before_request
def jGlobal():
  arr=(
    hook('Locale', cfg['Application']['Locale']),
    hook('host', socket.gethostname()),
    hook('flask_v', flask.__version__),
    hook('scaffolding_v', engine.__version__),
    hook('pl',pageLoadTime()),
    hook('cookie',getCookie()),
    # add here for more hook
  )
  return arr

# Bind in jinja_env template filter
def templateFilter():
  tf={
    "epochConvert":epochConvert,
    "epochConvertAll":epochConvertAll,
    "locale":locale,
  }
  return tf
