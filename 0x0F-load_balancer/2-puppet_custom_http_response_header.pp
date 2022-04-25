# Puppet manifest containing commands to automatically
# configure an Ubuntu machine

package { 'nginx':
ensure   => 'installed',
provider => 'apt',
}

file_line { 'Add the custom HTTP header':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'server_name _;',
line   => 'add_header X-Served-By $HOSTNAME;',
}



service { 'nginx':
ensure  => 'running',
require => Package['nginx'],
}
