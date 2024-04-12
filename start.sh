#!/bin/bash
echo -n Password:
read -s password
gunicorn --bind=0.0.0.0:9000 'app:myapp(phrase="'+$password+'")' --daemon