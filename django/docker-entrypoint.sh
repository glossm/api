#!/bin/sh
if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    /venv/bin/python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    /venv/bin/python manage.py collectstatic --noinput
fi

/venv/bin/uwsgi --ini uwsgi.ini

exec "$@"
