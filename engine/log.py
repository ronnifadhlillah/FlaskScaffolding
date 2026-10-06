from logging.handlers import RotatingFileHandler
from flask import Flask
import os
import logging

def configure_logging(app):
  if not app.debug:
    if not os.path.exists('../public/logs'):
      os.mkdir('../public/logs')
    file_handler = RotatingFileHandler(
      '../public/logs/error.log',
      maxBytes=10240,
      backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
      '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    file_handler.setLevel(logging.ERROR,logging.WARNING,logging.DEBUG)

    app.logger.addHandler(file_handler)

