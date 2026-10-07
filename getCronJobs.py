from apscheduler.schedulers.background import BackgroundScheduler

cron=BackgroundScheduler()
jobs = cron.get_jobs()
for job in jobs:
    print(f"ID: {job.id} | Nama: {job.name} | Next schedule: {job.next_run_time}")
