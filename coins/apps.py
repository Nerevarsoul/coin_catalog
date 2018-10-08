from django.apps import AppConfig

import django_rq


class CoinsConfig(AppConfig):
    name = 'coins'

    def ready(self):
        from .tasks import check_serie_amount, delete_coins

        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            job.delete()

        scheduler.cron('0 2 * * *', func=check_serie_amount, repeat=None)
        scheduler.cron(scheduled_time='0 1 * * *', func=delete_coins, repeat=None)
