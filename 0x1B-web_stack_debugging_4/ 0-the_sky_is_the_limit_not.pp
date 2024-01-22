# Fix the number of filedescriptor limit
exec {'Change the ulimit value':
        command => 'sed -i "s/15/1024/g" /etc/default/nginx; service nginx restart',
        path    => '/usr/bin:/bin'
}