# Replaces phpp by php

exec {'Remove a p':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
