from engine.build import init, hook
from engine.model import pageLoadTime
from flask import request,g
import urllib
import time
import flask
import socket
import configparser

cfg=configparser.ConfigParser()
cfg.read('config/app.py')

# Hooker is direct bind without going throught controller.
# you can directly parsing into view by calling it's 'key'

# hook(key, value) --> Sample
# Calling hook in jinja --> {{key}}

a=init()
@a.before_request
def jGlobal():
    arr=(
        hook('Locale', cfg['Application']['Locale']),
        hook('host', socket.gethostname()),
        hook('flask_v', flask.__version__),
        hook('pl',pageLoadTime()),
        # add here for more hook
    )
    return arr
