# Install flask 2.1.0 from pip3
package{ 'python3-pip':
  ensure => present,
}

package{ 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package{ 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],
}
