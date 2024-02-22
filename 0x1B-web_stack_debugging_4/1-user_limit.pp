# Increases the limit for user Holberton
exec { 'Hard limit increase':
  path    => '/bin',
  command => 'sed -i "s/nofile 5/nofile 7000/" /etc/security/limits.conf'
}

exec { 'Soft limit increase':
  path    => '/bin',
  command => 'sed -i "s/nofile 4/nofile 4096/" /etc/security/limits.conf'
}
