from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import configparser

cfg=çonfigparser.ConfigParser()
cfg.read('config/database.py')

def defineDriver():
    dd=cfg['Database']['Driver']
    if dd=='SQLite':
        drv='sqlite:///'+dd['dbName']+'?check_same_thread='+dd['CheckSameThread']
        return cnx(drv)

def cnx(driver):
    ce=create_engine(
        driver,
        pool_size=cfg['Database']['PoolSize'],
        max_overflow=cfg['Database']['MaxOverflow']
        )
    scp=scoped_session(sessionmaker(
        autocommit=cfg['Database']['AutoCommit'],
        autoflush=cfg['Database']['Autoflush'],
        bind=ce
    ))
    return scp

