# Client configuration file (w/ Puppet)
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile',
  require => Package['openssh-client'],
}

service { 'ssh':
  ensure  => 'running',
  enable  => true,
  require => Package['openssh-server'],
}
