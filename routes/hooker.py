from engine.build import init, hook
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
        # add here for more hook
    )
    return arr
