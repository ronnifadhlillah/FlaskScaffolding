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
  # add here for more cron
}
if cfg['Application']['cron']=="Enabled":
  cron.start()