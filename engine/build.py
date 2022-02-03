from flask import Flask,render_template,request
import datetime
import engine
import requests
import routes
import configparser
import werkzeug
import logging

cfg=configparser.ConfigParser()
cfg.read("config/app.py")

def init(test_config=None):
    return Flask(cfg['Application']['AppName'],
    template_folder=cfg['BootStrap']['Template'],
    static_folder=cfg['BootStrap']['Static'],
    instance_relative_config=True)

def build():
    a=init()
    beforeReq(a)
    connector=engine.defineDriver()
    jp(a)
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
    def before_first_request():
        print(datetime.datetime.now())

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

def handling_error(a):
    a.register_error_handler(404, page_not_found)
    a.register_error_handler(400, page_bad_request)
    a.register_error_handler(400, page_bad_request)

def page_not_found(errCode):
  return render_template('errorPage/404.jinja'), 404

def page_bad_request(errCode):
    return render_template('errorPage400.jinja'), 400

def page_rto(errCode):
    return render_template('errorPage/408.jinja'), 408
