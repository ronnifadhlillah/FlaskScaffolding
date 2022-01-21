from flask import Flask,render_template,request
import engine
import requests
import routes
import configparser
import werkzeug

cfg=configparser.ConfigParser()
cfg.read("config/App.ini")

def init(test_config=None):
    return Flask(cfg['Application']['AppName'],
    template_folder=cfg['BootStrap']['Template'],
    static_folder=cfg['BootStrap']['Static'],
    instance_relative_config=True)

def build():
    a=init()
    @a.before_request
    def bt():
        g=routes.jGlobal()
        jgp=g
        for jg in jgp:
            a.jinja_env.globals[jg['key']]=jg['value']
    @a.template_filter('epochConvert')
    def timeStampToStr(ts,format='%d/%m/%Y %H:%M:%S'):
        epoch=datetime.datetime.fromtimestamp(int(ts))
        if ts is None:
            return ""
        return epoch.strftime(format)
    connector=engine.defineDriver()
    jp(a)
    # if cfg['Auth']['default'] == True:
    if cfg['BootStrap']['Maintenance']=="True":
        err=engine.errCode
        a.register_blueprint(err.err)
        # print(cfg['BootStrap']['Maintenance'])
    else:
        aut=engine.auth
        w=routes.web
        a.register_blueprint(aut.bp)
        a.register_blueprint(w.bp)
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

def hook(k,v):
    arr={
        'key':k,
        'value':v
    }
    return arr

def handling_error(a):
    return a.register_error_handler(errcode, errDef)

# def page_not_found(e):
#   return render_template('404.jinja'), 404
def maintenanceMode(e):
  return render_template('503.jinja'), 503


def copyPat():
    apps=init()
    with apps.app_context():
        return request.url
