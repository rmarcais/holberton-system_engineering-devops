# Puppet manifest containing commands to automatically
# configure an Ubuntu machine

package { 'nginx':
ensure => present,
name   => 'nginx',
}

file_line { 'Add header':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'server_name _;',
line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
