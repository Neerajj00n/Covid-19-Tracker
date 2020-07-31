import requests
import json
from .models import *
from covid import Covid
#from schedule import Scheduler
#import schedule
import time 
import threading
#from background_task import background
from celery.schedules import crontab
from celery.task import periodic_task

@periodic_task(run_every=crontab(minute=0, hour='*/1'))
def data(): 
    try:
        covid = Covid(source="worldometers")
        cv = covid.get_data()
        for i in cv:
            cov = Covid19.objects.get(country=i['country'])
            cov.new_cases = i['new_cases']
            cov.new_deaths = i['new_deaths']
            cov.country = i['country']
            cov.confirmed=i['confirmed']
            cov.active=i['active']
            cov.deaths=i['deaths']
            cov.recovered=i['recovered']
            cov.save()
            print('ok')
        df = 'success'
        return  df
    except:
        result = "Failed"
        return result 

'''
def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run

Scheduler.run_continuously = run_continuously

def start_scheduler():
    scheduler = Scheduler()
    scheduler.every(60).minutes.do(data)
    scheduler.run_continuously()

#start_scheduler()

'''


#def new(request):
#    covid = Covid(source="worldometers")
#    cv = covid.get_data()
#    for i in cv:
#        Covid19.objects.create(country=i['country'],confirmed=i['confirmed'],active=i['active'],recovered=i['recovered'],deaths=i['deaths'],new_cases=i['new_cases'],new_deaths=i['new_deaths'])
#        print('ok')
#    df = 'done'
#    return  df     
#