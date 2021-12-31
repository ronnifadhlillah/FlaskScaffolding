from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import engine
import configparser
import os

cfg=configparser.ConfigParser()
cfg.read('config/Database.ini')

# Currently working in MariaDB / MySQL driver only

def defineDriver():
    dd=cfg['Database']['Driver']
    if dd !='SQLite':
        el=generalEngine(dd,cfg[dd]['Adaptor'],cfg[dd]['Dialect'])
        return el

def generalEngine(driver,adaptor,dialect):
    set=dialect+'+'+adaptor+'://'+cfg[driver]['Username']+':'+cfg[driver]['Password']+'@'+cfg[driver]['Host']+'/'+cfg[driver]['Name']
    return set

cnx=create_engine(defineDriver())
sessionLocal=scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=cnx))
