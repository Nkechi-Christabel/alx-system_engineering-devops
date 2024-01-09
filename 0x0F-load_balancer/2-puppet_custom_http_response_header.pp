# It automates the task of creating a custom HTTP header response.

exec { 'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure  => installed,
}
-> file_line { 'Add custom HTTP server':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By ${hostname};"
}
-> service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
