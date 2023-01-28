from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import configparser
import os

cfg=çonfigparser.ConfigParser()
cfg.read('config/database.py')

