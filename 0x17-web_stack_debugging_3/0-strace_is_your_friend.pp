# fix apache internal server error
exec { 'Fix 500 Error':
  command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
