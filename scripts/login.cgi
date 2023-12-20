#!/bin/bash

# Establecer valores de usuario y contraseña (reemplázalos con los valores correctos)
usuario_valido="lfss"
contrasena_valida="lfss"

shadow=$(sudo cat /etc/shadow)

# Obtener valores del formulario
read query_string

# Esto me funciona en home cat test.txt | awk -F'&' '{split($1, a, "=");print a[2]}'
username=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')
password=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')



# Verificar las credenciales
if [ "$username" == "$usuario_valido" ] && [ "$password" == "$contrasena_valida" ]; then
   
    whoami=$(whoami)
    echo "Content-type: text/html"
    echo ""
    echo "<html><body><h1>Login exitoso</h1>
    <h2>username:  $username /password:  $password </h2>   
    <p> $shadow </p> 
    <p> $whoami </p>
    </body></html>"
else
    echo "Status: 302 Found"
    echo "Location: ../failed_login.html"
    echo ""

fi


# Obtener información del usuario desde /etc/passwd
user_info=$(getent passwd "$username")

# Extraer el hash del password del campo de contraseña en /etc/shadow
password_hash=$(echo "$user_info" | cut -d: -f2)

# Hash del password proporcionado
provided_password_hash=$(echo -n "$password" | mkpasswd -s "$password_hash")