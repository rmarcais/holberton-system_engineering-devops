# Puppet manifest containing commands to automatically
# configure an Ubuntu machine

package { 'nginx':
ensure   => 'installed',
provider => 'apt',
}

file_line { 'Add header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}


service { 'nginx':
ensure  => 'running',
require => Package['nginx'],
}
