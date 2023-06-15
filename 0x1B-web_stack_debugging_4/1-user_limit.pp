#Puppet manifest to change OS configuration 
user { 'holberton':
  ensure     => present,
  managehome => true,
  shell      => '/bin/bash',
}

file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton hard nofile 10000\nholberton soft nofile 10000\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

exec { 'reload_limits':
  command     => 'sysctl --system',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.d/holberton.conf'],
}

service { 'ssh':
  ensure => running,
  enable => true,
}

