#!/bin/bash

# Establecer valores de usuario y contraseña (reemplázalos con los valores correctos)
usuario_valido="lfs"
contrasena_valida="lfs"

# Obtener valores del formulario
read query_string

# Esto me funciona en home cat test.txt | awk -F'&' '{split($1, a, "=");print a[2]}'
username=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')
password=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')

user_line=$(sudo cat /etc/shadow | grep $username)

salt=$(echo "$user_line" | awk -F'$' '{print $3}')

encrypted_password=$(openssl passwd -6 -salt $salt $password)



# Verificar las credenciales
if [ "$username" == "$usuario_valido" ] && [ "$password" == "$contrasena_valida" ]; then
   
    echo "Content-type: text/html"
    echo ""
    echo "<html><body><h1>Login exitoso</h1>
    <h2>username:  $username /password:  $password </h2> 
    <p> $salt </p>
    <p> $user_line </p>
    <p> ENCRYPTED:  $encrypted_password </p>
    </body></html>"
else
    echo "Status: 302 Found"
    echo "Location: ../failed_login.html"
    echo ""

fi
