# -*- coding: UTF-8  -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.local')
app = Celery('mysite')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

# load task modules from all registered Django app configs.
app.autodiscover_tasks(["coins"])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
