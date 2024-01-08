# It automates the task of creating a custom HTTP header response.

class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}
