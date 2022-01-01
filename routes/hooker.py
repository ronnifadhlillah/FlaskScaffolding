from engine.build import init, hook
from flask import request,g
import urllib
import time
import flask
import socket
import configparser

cfg=configparser.ConfigParser()
cfg.read('config/App.ini')

# Hooker is direct bind without going throught controller.
# you can directly parsing into view by calling it's 'key'

# hook(key, value) --> Sample

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

# if using def, write down below
def pageLoadTime():
    # we initialize the variable start
    # to store the starting time of
    # execution of program
    start = time.time()

    # we can take any program but for
    # example we have taken the below
    # program
    a = 0
    for i in range(1000):
        a += (i**100)

    # now we have initialized the variable
    # end to store the ending time after
    # execution of program
    end = time.time()
    pl=end-start
    return pl
