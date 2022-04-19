# Puppet manifest containing commands to automatically
# configure an Ubuntu machine

exec {'sudo apt-get -y update':
path => '/usr/bin',
}

exec {'sudo apt-get -y install nginx':
path => '/usr/bin',
}

exec {'sudo chown -R "$USER":"$USER" /var/www/html':
path => '/usr/bin',
}

exec {'echo "Hello World" > /var/www/html/index.nginx-debian.html':
path => '/usr/bin',
}

exec {'sed -i "/server_name _;/a location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }" /etc/nginx/sites-available/default':
path => '/usr/bin',
}

exec {'service nginx restart':
path => '/usr/sbin',
}
