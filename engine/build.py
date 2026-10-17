from flask import Flask,session,g,render_template
from engine.database import defineDriver
from engine.hooker import jGlobal,templateFilter
from engine.session import cacheMid
from flask_caching import Cache
import routes
import configparser
import os
# import cron

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

  cacheSwitcher=cfg['Cache']['Enabled']
  if cacheSwitcher=="Enabled":

    # Cache using filesystem (global config)
    cache=Cache(config={
      "DEBUG": cfg['Cache']['Debug'],
      "CACHE_TYPE": "FileSystemCache",
      "CACHE_DEFAULT_TIMEOUT": int(cfg['Cache']['Timeout']),
      "CACHE_THRESHOLD":  int(cfg['Cache']['Threshold']),
      "CACHE_DIR": os.path.join(os.getcwd(),cfg['Cache']['Directory'])
    })

    cache.init_app(a)
    cacheMid(a,cache)

  defineDriver()
  jp(a)
  handling_error(a)
  # enablingCron
  # cron()

# ================================================================
  # Registering model / route below
  # Registering Blueprint sample
    
  aut=routes.auth
  a.register_blueprint(aut.bp)
    
  # General routes / Routes for all
  w=routes.web
  a.register_blueprint(w.bp)
# ================================================================
    
  @a.before_request
  def load_logged_in_user():
    username=session.get("id")
    if username is None and "id" not in session:
      g.id=None
    else:
      g.id=username
      
  def bt():
    g=jGlobal()
    jgp=g
    for jg in jgp:
      a.jinja_env.globals[jg['key']]=jg['value']

  for b,c in templateFilter().items():
    a.jinja_env.filters[b]=c

  return a
  
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

# Defining error page
def handling_error(a):
  a.register_error_handler(401, need_login)
  a.register_error_handler(403, permission)
  a.register_error_handler(404, page_not_found)

def need_login(errCode):
  return render_template('errorPage/404.jinja'), 401

def permission(errCode):
  return render_template('errorPage/404.jinja'), 403

def page_not_found(errCode):
  return render_template('errorPage/404.jinja'), 404

