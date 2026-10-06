from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from engine.model import randStr

cron=BackgroundScheduler()

def randomNumber():
  return randStr("TEST_PREFIX")

# registering CRON below
def startCron(y,default="No"):
  if y=="No":
    pass
  else:
    scheduler.add_job(openPoReminderCron, 'cron', day_of_week='mon-sun', hour=1, minute=0)
    scheduler.start()
