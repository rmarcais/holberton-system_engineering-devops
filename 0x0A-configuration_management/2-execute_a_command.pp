# Creates a manigest that kills a process named killmenow

exec { 'kill process':
command => 'pkill -f killmenow',
path    => '/usr/bin',
}
