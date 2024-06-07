python3

on ubuntu22
 source .env/bin/activate

 ps -lA | grep gunicorn
 
cd /var/www/testpy/
 source .env/bin/activate
 bbb --bind=0.0.0.0:9000 g_app:app
  
  

no local testin..testing on live  
   
cd /var/www/testpy/
 source .env/bin/activate
 python3 skale_cron.py

debug
sudo su
crontab -e
/var/www/testpy/.env/bin/python3 /var/www/testpy/skale_cron.py

 /var/log/syslog





flask --app g_app run
gunicorn --bind=0.0.0.0:9000 'app:myapp' dddddasd


 ** apply sudo **






ps -lA | grep super

kill 1059171
supervisord -c supervisord.conf --loglevel=debug --logfile=log.txt
supervisorctl reread

https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18