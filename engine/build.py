from flask import Flask,session,g,render_template
from engine.database import defineDriver
from engine.hooker import jGlobal,templateFilter
import configparser
import cron

cfg=configparser.ConfigParser()
cfg.read("config/app.py")

def init(test_config=None):
    return Flask(cfg['Application']['AppName'],
    template_folder=cfg['BootStrap']['Template'],
    static_folder=cfg['BootStrap']['Static'],
    instance_relative_config=True)

# Build function is a whole body of the framework. Every part is connect or linked to this function.
def build():
    a=init()
    beforeReq(a)
    defineDriver()
    jp(a)
    handling_error(a)
    # enablingCron
    cron()
      

    

    @a.before_request
    def load_logged_in_user():
      username=session.get("id")
      if username is None and "id" not in session:
        g.id=None
      else:
        g.id=username

    for b,c in templateFilter().items():
      a.jinja_env.filters[b]=c
    return a

def beforeReq(a):
    @a.before_request
    def bt():
        g=jGlobal()
        jgp=g
        for jg in jgp:
            a.jinja_env.globals[jg['key']]=jg['value']

# # ================================================================
# # Registering model / route below




# # ================================================================
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

def handling_error(a):
    a.register_error_handler(404, page_not_found)

# Defining error page
def page_not_found(errCode):
    return render_template('errorPage/404.jinja'), 404

