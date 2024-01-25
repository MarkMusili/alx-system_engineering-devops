# Allow holberton user to open files concurently
exec {
    command => 's/5/4096/g' /etc/security/limits.conf
    path    => '/usr/local/bin/:/bin/'
}

exec {
    command => 's/4/4096/g' /etc/security/limits.conf
    path    => '/usr/local/bin/:/bin/'
}
