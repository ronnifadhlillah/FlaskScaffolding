from flask import redirect,render_template,session,request,url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
import imaplib
from engine.database import sessionLocal
from engine.build import init

# class authentication():
#     def __init__(self,adapter,un,ps):
#         strValidation(self.un,self.ps)
#         doLogin()
#         # build session
#         session()
#         # redirect template
#         return redirect(self.temp)


def strValidation(self,un,ps):
    # Make input value of username and password as a string.
    # prevent sql hijacking
    v={
        un:"""%s""" % str(self.un),
        ps:"""%s""" % str(self.ps)
    }
    return v

def doLogin(bp):
    # login Query
    # @bp.route('/login',methods=['POST'])
    # def loginHandler():
    #     return render_template('auth.jinja')
    # q=text("""SELECT * FROM %s WHERE %s=%s AND %s=%s"""%(auth['table'],auth['username'],v['un'],auth['password'],v['ps']))
    # r=sessionLocal.execute(q)
    # for row in r:
    #     print(row['username'])
    # if row count > 1
        # return True
    # else:
        # return False
        # guard attempt
    pass

def session():
    # session maker
    pass

def guard():
    # Three times input submit
    return render_template(loginPage)
    pass

def logout():
    # destroy logout session
    pass

def imapConnector(self,srv,inp):
    # All validation must execute here.
    try:
        imp=imaplib.IMAP4_SSL(self.srv,port=995)
        imp.login(self.un,self.ps)
        return True
    except imaplib.IMAP4.error:
        print('Imap Conection fail. Maybe username and password is wrong.')
        return False
