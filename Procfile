web: gunicorn FakeCSV.wsgi --log-file -
worker: celery worker --app=tasks.app
