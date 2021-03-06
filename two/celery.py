from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'two.settings')
app = Celery('two')
app.config_from_object('django.conf:settings', namespace='')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

