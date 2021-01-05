web: gunicorn fake_csv.wsgi --log-file -
worker: celery --app fake_csv.celery.app worker --loglevel info
