from datetime import datetime

from django.apps import AppConfig

import django_rq

from .tasks import *


class CoinsConfig(AppConfig):
    name = 'coins'

    def ready(self):
        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            job.delete()

        scheduler.schedule(datetime.utcnow(), check_serie_amount, interval=60*5) 

