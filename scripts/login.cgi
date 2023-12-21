#!/bin/bash

# Obtener valores del formulario
read query_string

# Esto me funciona en home cat test.txt | awk -F'&' '{split($1, a, "=");print a[2]}'
username=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')
password=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')

user_line=$(sudo cat /etc/shadow | grep $username)

shadow_user=$(echo "$user_line" | awk -F':' '{print $1}')
hashed_password=$(echo "$user_line" | awk -F':' '{print $2}')

salt=$(echo "$user_line" | awk -F'$' '{print $3}')

encrypted_password=$(openssl passwd -6 -salt $salt $password)

# Verificar las credenciales
if [ "$username" == "$shadow_user" ] && [ "$encrypted_password" == "$hashed_password" ]; then
    echo "Status: 302 Found"
    echo "Location: ../home.html"
    echo ""
    #echo "Content-type: text/html"
    #echo ""
    #echo "<html><body><h1>Login exitoso</h1>
    #<h2>username:  $username /password:  $password </h2> 
    #<p>SALT=  $salt </p>
    #<p> SHADOW USER = $shadow_user </p>
    #<p> LINE = $user_line </p>
    #<p> HASHED = $hashed_password </p>
    #<p> ENCRYPTED:  $encrypted_password </p>
    #</body></html>"
else
    echo "Status: 302 Found"
    echo "Location: ../failed_login.html"
    echo ""

fi
