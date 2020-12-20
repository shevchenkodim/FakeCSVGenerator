web: gunicorn FakeCSV.wsgi --log-file -
celery: celery worker -A FakeCSV -l info -c 4
