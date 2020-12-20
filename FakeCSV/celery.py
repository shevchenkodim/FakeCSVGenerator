import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FakeCSV.settings')

app = Celery('FakeCSV')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
     enable_utc=True,
     timezone='Europe/Kiev',
)
app.autodiscover_tasks()
