from engine import init,hook
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
        # add here for more hook
    )
    return arr
