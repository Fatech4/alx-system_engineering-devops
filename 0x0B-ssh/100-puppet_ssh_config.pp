# Client configuration file (w/ Puppet)
file { '/etc/ssh/sshd_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
  notify  => Service['ssh'],
}

service { 'ssh':
  ensure  => running,
  enable  => true,
  require => File['/etc/ssh/sshd_config'],
}
