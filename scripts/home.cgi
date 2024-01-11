#!/bin/bash

echo 'Content-type: text/html'
echo ''
echo '<!DOCTYPE html>'
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/home.css"/>'
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
echo '<link rel="icon" href="../icons/Hasbulla.png" type="image/png">'
echo '</head>'
echo '<body>'

who=$(head -n 1 user.log)
echo '<header>'
echo "<div class='welcome'> Welcome $who </div>"
echo '<div class="buttons">'
echo '<form action="./restart.sh" method="post"><button class="restart" type="submit">Restart</button></form>'
echo '<form action="./shutdown.sh" method="post"><button class="shutdown" type="submit">Sutdown</button></form>'
echo '</div>'
echo '</header>'
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo "</section>"
echo '<div class="wrapper">'
# Monitoring ----------------------------------------------------------------------- 
cpu_usage=$(top -bn1 | awk '/%Cpu/ {print $1, $3, $6, $8}' |  sed 's/%//g')
last_ten_users=$(awk '/WEBASO/' /var/log/sys.log | grep "has logged in"| tail -n 10 )
ram=$(free -m | awk '/Mem/ {print $3,"/" $2}')
disc=$(df -h | awk '{print $0"<br>"}')

echo '  <div class="monitoring">'
echo '    <p>Monitoring</p>'
echo '    <div class="monitoring_wrapper">'
echo '       <div class="monitoring_item_wrapper">'
echo '          <div class="monitoring_item">'
echo "                  Overall CPU Usage $cpu_usage"
echo '          </div>'
echo "          <div class="monitoring_item">RAM: $ram Gb </div>"
echo -e "          <div class='monitoring_item'>$disc</div>"
echo '          <div class="monitoring_item">Last 10 Users:</div>'
while IFS= read -r line; do
  printf '          <div class="monitoring_user_item">%s</div>\n' "$line"
done <<< "$last_ten_users"
echo '       </div>'
echo '    </div>'
echo '  </div>'
# Menu ------------------------------------------------------------------------------
echo '  <div class="menu">'
# Process handling
echo '    <div class="menu_item">'
echo '     <p>Process handling</p>'
echo '    <form action="./process_management.cgi" method="post"><button class="See" type="submit">See</button></form>'
echo '    </div>'
# Logs 
echo '    <div class="menu_item">'
echo '     <p>Logs</p>'
echo '    <form action="./logs.cgi" method="post"><button class="See" type="submit">See</button></form>'
echo '    </div>'
# Users
echo '    <div class="menu_item">'
echo '      <p>Users management</p>'
echo '     <form action="./user_management.cgi" method="post"><button class="See" type="submit">See</button></form>'
echo '    </div>'
# Packet filtering
echo '    <div class="menu_item">'
echo '      <p>Packet filtering</p>'
echo '       <form action="./packet_filtering.cgi" method="post"><button>See</button></form>'
echo '    </div>'
# Cron
echo '    <div class="menu_item">'
echo '      <p>Cron management</p>'
echo '        <form action="./cron_management.cgi" method="post"><button>See</button></form>'
echo '    </div>'
# Music
echo '    <div class="menu_item">'
echo '      <p>Music</p>'
echo '      <button>See</button>'
echo '    </div>'
echo '  </div>'
echo '</div>'
echo '</body>'
echo '</html>'
echo ''
