#!/bin/bash

echo 'Content-type: text/html'
echo ''
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/home.css"/>'
echo '</head>'
echo '<body>'

who=$(head -n 1 user.log)
echo '<header>'  
echo "<div class='welcome'> Welcome $who </div>"
echo '<div class="buttons">'
# IDK if i can use javascript to call the scripts or not 
# MAYBE I SHOULD USE POST OR GET TO CALL THE SCRIPTS
echo '<form action="./restart.sh" method="post"><button class="restart" type="submit">Restart</button></form>'
echo '<form action="./shutdown.sh" method="post"><button class="shutdown" type="submit">Sutdown</button></form>'
echo '</div>'
echo '</header>'
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo '<div class="menu">'
# Process handling
echo '  <div class="menu_item">'
echo '    <p>Process handling</p>'
echo '    <button>See</button>'
echo '  </div>'
# Monitoring 
echo '  <div class="menu_item">'
echo '    <p>Monitoring</p>'
echo '    <button>See</button>'
echo '  </div>'
# Logs 
echo '  <div class="menu_item">'
echo '    <p>Logs</p>'
echo '    <button>See</button>'
echo '  </div>'
# Users
echo '  <div class="menu_item">'
echo '    <p>Users management</p>'
echo '    <button>See</button>'
echo '  </div>'
# Packet filtering
echo '  <div class="menu_item">'
echo '    <p>Packet filtering</p>'
echo '    <button>See</button>'
echo '  </div>'
# Cron
echo '  <div class="menu_item">'
echo '    <p>Cron management</p>'
echo '    <button>See</button>'
echo '  </div>'
# Music
echo '  <div class="menu_item">'
echo '    <p>Music</p>'
echo '    <button>See</button>'
echo '  </div>'
echo '</div>'
echo '</body>'
echo '</html>'
echo ''
