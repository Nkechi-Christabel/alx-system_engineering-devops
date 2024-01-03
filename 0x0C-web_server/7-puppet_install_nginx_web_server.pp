#!/usr/bin/env bash
# Installs and configure an Nginx server using Puppet instead of Bash.

package { 'nginx':
 ensure => present,
}

file { '/var/www/html/index.html':
 ensure  => file,
 content => "Hello World!\n",
}

service { 'nginx':
 ensure  => running,
 enable  => true,
 require => Package['nginx'],
}

file_line { 'nginx_redirect_me':
 path  => '/etc/nginx/sites-available/default',
 line  => 'location /redirect_me { return 301 http://www.example.com/new-page; }',
 after => 'location / {',
 notify => Service['nginx'],
}
