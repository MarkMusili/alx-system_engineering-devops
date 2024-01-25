# Allow holberton user to open files concurently
exec { 'increase_nofile_limits':
  command => '/bin/sed -i -e "s/5/4096/g" -e "s/4/4096/g" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}
