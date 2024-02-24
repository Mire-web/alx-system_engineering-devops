# Kill current running process
exec{'killmenow':
  command => '/bin/pkill -15 $(pidof killmenow)',
}
