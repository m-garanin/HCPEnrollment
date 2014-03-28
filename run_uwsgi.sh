#!/bin/sh
uwsgi -w run_uwsgi -p 4 -M -t 20 -R 1000 -d /home/www/log/hcp2_uwsgi.log --pidfile /home/www/hcp2_uwsgi.pid  -s 127.0.0.1:9320
