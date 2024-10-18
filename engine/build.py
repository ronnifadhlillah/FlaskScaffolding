from flask import Flask,render_template,request,session
from datetime import datetime,timedelta
import engine
import routes
import configparser
import werkzeug

cfg=configparser.ConfigParser()
cfg.read("config/app.py")

def init(test_config=None):
    return Flask(cfg['Application']['AppName'],
    template_folder=cfg['BootStrap']['Template'],
    static_folder=cfg['BootStrap']['Static'],
    instance_relative_config=True)

# Build function is a whole body of the framework. Every part is connect or linked to this function.
def build():
    # First Initialize
    a=init()

    # Before
    beforeReq(a)

    # Database Connector
    engine.defineDriver()

    # Jinja Properties
    jp(a)

    # Error handler
    handling_error(a)

    # General routes / Routes for all
    w=routes.web
    a.register_blueprint(w.bp)

    return a

def beforeReq(a):
    @a.before_request
    def bt():
        g=routes.jGlobal()
        jgp=g
        for jg in jgp:
            a.jinja_env.globals[jg['key']]=jg['value']

    @a.before_request
    def sessionLifetime():
        engine.sessionLifetime(a)

    @a.before_request
    def sessionLoader():
        engine.loadCurrentUser()

def jp(a):
    if cfg['Application']['Debug']=="True":
        bool=True
    else:
        bool=False
    a.config['DEBUG']=bool
    a.config['ENV']=cfg['Application']['Environment']
    a.config['SECRET_KEY']=cfg['Application']['SecretKey']
    a.secret_key=cfg['Application']['SecretKey']
    a.jinja_env.auto_reload=bool
    if cfg['URI']['Set']=="True":
        a.config['SERVER_NAME']=cfg['URI']['Url']+':'+cfg['URI']['Port']

def hook(k,v):
    arr={
        'key':k,
        'value':v
    }
    return arr
