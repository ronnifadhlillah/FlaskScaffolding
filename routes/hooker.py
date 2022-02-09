from engine import init,hook,pageLoadTime
import flask
import socket
import configparser
import engine

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
        hook('scaffolding_v', engine.__version__),
        hook('pl',pageLoadTime()),
        hook('cookie',engine.getCookie()),
        # add here for more hook
    )
    return arr
