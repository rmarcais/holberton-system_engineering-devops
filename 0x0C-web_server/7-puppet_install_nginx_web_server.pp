# Puppet manifest containing commands to automatically
# configure an Ubuntu machine

package { 'nginx':
ensure   => 'installed',
provider => 'apt',
}

file { 'Hello World':
ensure  => 'present',
path    => '/var/www/html',
content => 'Hello World\n',
}

file_line { 'Add the redirect_me page':
ensure => 'present',
path   => '/var/www/html/index.nginx-debian.html',
after  => 'server_name _;',
line   => 'location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }',
}

exec { 'service nginx restart':
path => '/usr/sbin'
}
