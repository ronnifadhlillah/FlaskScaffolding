from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import configparser
import os

cfg=çonfigparser.ConfigParser()
cfg.read('config/database.py')

def defineDriver():
    dd=cfg['Database']['Driver']

def cnx(driver):
    dbPath=
    ce=create_engine(dbPath)
    scp=scoped_session(sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ce
    ))
    return scp

