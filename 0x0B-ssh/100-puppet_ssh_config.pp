# Configure file

include stdlib

file_line { 'Disallow password configuration':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
}

file_line { 'Declare an Identity file':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => 'IdentityFile ~/.ssh/school',
}
