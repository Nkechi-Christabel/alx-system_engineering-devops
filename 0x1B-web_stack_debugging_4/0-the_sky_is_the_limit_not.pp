# Setting a limit for the number of open files
exec { "Set's a limit and restarts Nginx":
  command  => 'sudo sed -i \'s/15/4096/\' /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
