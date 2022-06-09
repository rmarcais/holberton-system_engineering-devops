# Remove lines

exec {'Remove line':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sed -i "s/holberton/#holberton/" /etc/security/limits.conf',
}
