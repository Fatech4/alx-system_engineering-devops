# Client configuration file (w/ Puppet}
package { 'augeas-tools':
  ensure => installed,
}

file { '/etc/ssh/sshd_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['ssh'],
  require => Package['augeas-tools'],
  before  => Service['ssh'],
}

augeas { 'sshd_config':
  context => '/files/etc/ssh/sshd_config',
  changes => [
    'set * IdentityFile ~/.ssh/school',
    'set * PasswordAuthentication no',
  ],
  require => File['/etc/ssh/sshd_config'],
}

service { 'ssh':
  ensure  => running,
  enable  => true,
  require => Augeas['sshd_config'],
}

