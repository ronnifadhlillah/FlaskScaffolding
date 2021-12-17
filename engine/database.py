from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import engine
import configparser
import os

cfg=configparser.ConfigParser()
cfg.read('config/Database.ini')

# Currently working in MariaDB / MySQL driver only

def DefineDriver():
    dd=cfg['Database']['Driver']
    if dd !='SQLite':
        el=GeneralEngine(dd,cfg[dd]['Adaptor'],cfg[dd]['Dialect'])
        return el

def GeneralEngine(driver,adaptor,dialect):
    unite=dialect+'+'+adaptor+'://'+cfg[driver]['Username']+':'+cfg[driver]['Password']+'@'+cfg[driver]['Host']+'/'+cfg[driver]['Name']
    return unite

cnx=create_engine(DefineDriver())
sessionLocal=scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=cnx))
