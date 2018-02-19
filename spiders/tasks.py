from django_rq import job

from .models import *

__all__ = ('run_spiders',)


@job
def run_spiders():
    spiders = Spider.objects.filter(is_active=True)
    for spider in spiders:
        spider.run()
