from django.apps import AppConfig

import django_rq


class SpidersConfig(AppConfig):
    name = 'spiders'

    def ready(self):
        from .tasks import run_spiders

        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            job.delete()

        scheduler.cron('0 2 * * *', run_spiders)
