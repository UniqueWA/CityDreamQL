web: newrelic-admin run-program gunicorn -b "0.0.0.0:$PORT" -w 3 CityDreamQL.wsgi
release: python manage.py migrate
