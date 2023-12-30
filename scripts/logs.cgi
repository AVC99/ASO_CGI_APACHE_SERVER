#!/bin/bash

who=$(head -n 1 user.log)
echo -e "User: $who has entered the logs page" >> ./register.log

echo 'Content-type: text/html'
echo ''
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/logs.css"/>'#echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
echo '<link rel="icon" href="../icons/Hasbulla.png" type="image/png">'
echo '</head>'

echo '<body>'

echo "<header><form class='form_button'  action='home.cgi' method='post'><button type='submit' name='user' value='$who'>Home</button></form>
<p class='title'>logs</p>
</header>"
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo "</section>"
echo '<div class="wrapper">'
user_log=$(cat ./register.log | awk '{print $0"<br>"}')
echo '    <div class="logs">'
echo "    $user_log"
echo "    </div>"
echo "    <div class='syslog'>"
echo "    $(sudo cat /var/log/auth.log | awk '/sudo/ || /sshd/ {print $0"<br>"}')"
echo "    </div>"
echo "</div>"
echo '</body>'
echo '</html>'
echo ''