#client configuration using puppet


file { 'Turn off passwd auth':
  ensure => present,
  line   => '    PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}

file { 'Declare identity file':
  ensure => present,
  line   => '    IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}
