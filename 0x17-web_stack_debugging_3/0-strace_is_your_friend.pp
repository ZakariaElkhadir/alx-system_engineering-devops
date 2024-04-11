package { 'apache2': ensure => 'installed'}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Package['apache2'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello, World!',
  require => Package['apache2'],
}


