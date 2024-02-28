#client configuration using puppet

file { 'turn off password authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file { 'declare identity file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

