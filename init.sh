#!/usr/bin/env bash
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ~/web/ask
python3 manage.py makemigrations
python3 manage.py migrate
gunicorn --bind 0.0.0.0:8000 ask.wsgi:application
