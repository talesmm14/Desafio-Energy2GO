import os

from celery import Celery

from config.settings import TIME_ZONE

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = TIME_ZONE
app.autodiscover_tasks()
