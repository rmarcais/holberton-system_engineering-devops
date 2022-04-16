# Sets up our client SSH configurationfile

file_line {'Use private key':
path => '/etc/ssh/ssh_config',
line => '	IdentityFile ~/.ssh/school',
}

file_line {'Refuse password':
path => '/etc/ssh/ssh_config',
line => '	PasswordAuthentication no',
}
