# File: 0-the_sky_is_the_limit_not.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Manage Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Manage additional Nginx configuration files
file { '/etc/nginx/conf.d/':
  ensure  => directory,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  recurse => true,
  purge   => true,
  notify  => Service['nginx'],
}

# Manage Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
