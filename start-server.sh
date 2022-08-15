#!/usr/bin/env bash
# start gunicorn http server
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd webapp; python manage.py createsuperuser --no-input)
fi
(cd webapp; gunicorn webapp.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"