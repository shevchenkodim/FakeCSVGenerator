web: gunicorn FakeCSV.wsgi --log-file -
worker: celery -A FakeCSV worker -B --loglevel=info
