#INSTALL flask from pip3
exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  creates => '/usr/local/lib/python3.8/dist-packages/flask',
}
