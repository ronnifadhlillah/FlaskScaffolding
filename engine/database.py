from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import engine
import configparser
import os

cfg=configparser.ConfigParser()
cfg.read('config/database.py')

# Currently working in MariaDB / MySQL driver only

def defineDriver():
    # Database connector example
    set='mariadb+mariadbconnector://root@localhost/test'
    return set


def generalEngine(driver,adaptor,dialect):
    set=dialect+'+'+adaptor+'://'+cfg[driver]['Username']+':'+cfg[driver]['Password']+'@'+cfg[driver]['Host']+'/'+cfg[driver]['Name']
    return set

cnx=create_engine(defineDriver())
sessionLocal=scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=cnx))
