from datetime import datetime

from django.apps import AppConfig

import django_rq


class CoinsConfig(AppConfig):
    name = 'coins'

    def ready(self):
        from .tasks import check_serie_amount

        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            job.delete()

        scheduler.cron('0 2 * * *', check_serie_amount) 

