sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c ~/web/etc/hello.py --bind 0.0.0.0:8080 hello:app &
gunicorn -c ~/web/ask --bind 0.0.0.0:8000 ask:wsgi
