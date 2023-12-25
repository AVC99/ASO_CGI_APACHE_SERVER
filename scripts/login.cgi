#!/bin/bash
# Obtener valores del formulario
read query_string
username=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')
password=$(echo "$query_string" | awk -F'&' '{split($2,a,"="); print a[2]}')
user_line=$(sudo cat /etc/shadow | grep "$username")
shadow_user=$(echo "$user_line" | awk -F':' '{print $1}')
hashed_password=$(echo "$user_line" | awk -F':' '{print $2}')
salt=$(echo "$user_line" | awk -F'$' '{print $3}')
encrypted_password=$(openssl passwd -6 -salt $salt $password)
# Verificar las credenciales
if [ "$username" == "$shadow_user" ] && [ "$encrypted_password" == "$hashed_password" ]; then
    # TODO: Create persitent file 
    
    echo "Status: 302 Found"
    echo "Location: ./home.cgi"
    echo ""
else
    echo "Status: 302 Found"
    echo "Location: ../failed_login.html"
    echo ""
fi
