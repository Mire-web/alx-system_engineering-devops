# Script to increase nginx file limits
exec {'Increase Ulimit nginx':
  command => 'sed -i "s/ULIMIT=.*/ULIMIT=\"-n 4096\"" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec {'restart nginx':
  command => 'service nginx restart',
  path    => '/etc/init.d'
}
