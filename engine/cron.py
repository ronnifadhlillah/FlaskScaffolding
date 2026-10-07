from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from engine.model import randStr
import configparser

cfg=configparser.ConfigParser()
cfg.read("config/app.py")
cron=BackgroundScheduler()

def randomNumber():
  return randStr("TEST_PREFIX")

# registering CRON below
jobs={
  "j1":cron.add_job(randomNumber, 'cron', day_of_week='mon-sun', hour=1, minute=0),
  "j2":cron.add_job(t1, 'cron', day_of_week='mon-sun', hour=1, minute=0),
  "j3":cron.add_job(t2, 'cron', day_of_week='mon-sun', hour=1, minute=0),
  "j4":cron.add_job(t3, 'cron', day_of_week='mon-sun', hour=1, minute=0)
}

cron.start()