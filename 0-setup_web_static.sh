#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Insert simple content into the html file
echo "shera" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set the ownership and permission of the data file
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Set the Nginx configuration file
# nginx_config="/etc/nginx/sites-available/default"

# Update the Nginx Config to use the alias directive
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart