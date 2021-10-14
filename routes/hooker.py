from engine.build import Init, Hook
import flask
import socket
import configparser

cfg=configparser.ConfigParser()
cfg.read('config/App.ini')

# Hooker is direct bind without going throught controller.
# you can directly parsing into view by calling it's 'key'

# hook(key, value) --> Sample

a=Init()
@a.before_request
def Jglobal():
    arr=(
        Hook('Locale', cfg['Application']['Locale']),
        Hook('host', socket.gethostname()),
        Hook('flask_v', flask.__version__),
        # add here for more hook
    )
    return arr
