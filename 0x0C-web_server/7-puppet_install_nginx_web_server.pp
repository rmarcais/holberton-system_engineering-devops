# Puppet manifest containing commands to automatically
# configure an Ubuntu machine

package { 'nginx':
ensure   => 'installed',
provider => 'apt',
}

file { '/var/www/html/index.nginx-debian.html':
ensure => 'present',
path => '/var/www/html'
content => 'Hello World\n',
}

file_line { 'Add the redirect_me page':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'server_name _;',
line   => 'location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }',
}

service { 'nginx':
ensure  => 'running',
require => Package['nginx'],
}
