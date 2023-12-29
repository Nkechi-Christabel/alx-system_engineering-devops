# It sets up the client's SSH configuration file so that you can
# connect to a server without typing a password.

file_line { 'SSH configuration':
  path => '/etc/ssh/ssh_config',
  line => "Host *\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n"
}
