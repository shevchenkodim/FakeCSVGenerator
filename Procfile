web: gunicorn FakeCSV.wsgi --log-file -
worker: celery -E --app FakeCSV.celery.app worker
