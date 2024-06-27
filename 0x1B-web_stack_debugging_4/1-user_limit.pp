exec {'Increase-hard-limit':
  command => 'sed -i "/holberton/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec {'Increase-soft-limit':
  command => 'sed -i "/holberton/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
