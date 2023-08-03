from apscheduler.schedulers.background import BackgroundScheduler
from dashbaord.earnings import earning_job

def start():
    scheduler =BackgroundScheduler()
    scheduler.add_job(earning_job,'interval',seconds=10)
    scheduler.start()