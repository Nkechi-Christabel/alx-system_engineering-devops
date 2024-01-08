# It automates the task of creating a custom HTTP header response.

package { 'nginx':
  ensure => installed,
}

$hostname = $::hostname

augeas { 'nginx_custom_header':
  context => '/etc/nginx/sites-available/default/',
  changes => [
    "set add_header 'X-Served-By $hostname'",
  ],
  notify => Service['nginx'],
  require => Package['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Augeas['nginx_custom_header'],
}
