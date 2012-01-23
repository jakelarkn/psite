# Config file for gunicorn server
#bind = "173.255.241.157:80"
bind = 'unix:/tmp/gunicorn.sock'

workers = 4
