#!/bin/bash

read query_string
user=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')

who=$(head -n 1 user.log)
echo -e "User: $who has removed: $user" >> ./register.log

#PROTECTED USERS
protected_users=("root" "bin" "deamon" "messagebus" "uuidd" "nobody" "tester" "sshd" "apache" "dhcpcd")

if [[ " ${protected_users[@]} " =~ " $user " ]]; then
        output=$(echo "User $user is protected and cannot be removed.")
    else
        # Remove the user if not protected
        sudo userdel -r "$user"
        output=$(echo "User $user removed successfully.")
    fi

#RETURNING TO THE PROCESS MANAGEMENT PAGE
echo 'Content-type: text/html'
echo ''
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/user_management.css"/>'
echo '<link rel="icon" href="../icons/Hasbulla.png" type="image/png">'
echo '</head>'

echo '<body>'
echo "<header><form class='form_button'  action='./home.cgi' method='post'><button type='submit' name='user' value='$who'>Home</button></form>
<p class='title'>User Management</p>
</header>"
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo "</section>"
users=$(cat /etc/passwd | cut -d: -f1)
echo '<div class="wrapper">'

echo '  <div class="user_tool">'
echo "<div class='output'>$output</div>"
echo '    <form action="./add_user.sh" method="post">'
echo '      <input type="text" name="user" id="user" placeholder="Username" required/>'
echo '      <button type="submit" name="remove">Add</button>'
echo '    </form>'
echo '    <form action="./remove_user.sh" method="post">'
echo '      <input type="text" name="username" id="username" placeholder="Username" required/>'
echo '      <button type="submit" name="remove">Remove</button>'
echo '    </form>'
echo '  </div>'
echo '  <div class="table">'
echo "    <div class='user_list'>"
echo "      <pre>$users</pre>"
echo "    </div>"
echo '  </div>'
echo "</div>"
echo '</body>'
echo '</html>'
echo ''