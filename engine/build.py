from flask import Flask,render_template
import engine
import routes
import os
import configparser

cfg=configparser.ConfigParser()
cfg.read("config/App.ini")

def Init(test_config=None):
    return Flask(cfg['Application']['AppName'],
    template_folder=cfg['BootStrap']['Template'],
    static_folder=cfg['BootStrap']['Static'],
    instance_relative_config=True)

def Build():
    a=Init()
    @a.before_request
    def Br():
        g=routes.Jglobal()
        jgp=g
        for jg in jgp:
            a.jinja_env.globals[jg['key']]=jg['value']
    @a.template_filter('epochConvert')
    def epochConverter(ts,format='%d/%m/%Y %H:%M'):
        epoch=datetime.datetime.fromtimestamp(int(ts))
        if ts is None:
            return ""
        return epoch.strftime(format)
    connector=engine.DefineDriver()
    Jp(a)
    a.register_error_handler(404, page_not_found)
    engine.init_app(a)
    return a

def Jp(a):
    if(cfg['Application']['Debug'])=="True":
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

def Hook(k,v):
    arr={
        'key':k,
        'value':v
    }
    return arr

def page_not_found(e):
  return render_template('404.html'), 404
