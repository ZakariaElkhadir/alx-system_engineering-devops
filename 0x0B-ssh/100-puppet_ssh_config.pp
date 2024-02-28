#client configuration using puppet

file { '~/.ssh/school':
  ensure => present,
}
