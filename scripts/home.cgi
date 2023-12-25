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

who=$(whoami)
echo '<header>'  
echo "<div class='welcome'> Welcome $who </div>"
echo '<div class="buttons">'
# IDK if i can use javascript to call the scripts or not 
# MAYBE I SHOULD USE POST OR GET TO CALL THE SCRIPTS
echo '<button class="restart" type="button" onclick="window.location.href='../scripts/restart.cgi'">Restart</button>'
echo '<button class="shutdown" type="button" onclick="window.location.href='../scripts/shutdown.cgi'">Sutdown</button>'
echo '</div>'
echo '</header>'
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo '<div class="signin">'
echo '<div class="content">'
# MAKE A GRID OF SHIT TO DO and we good 
echo '<h2>HOME</h2>'
echo '<h3>ASO Server</h3>'
echo '</div>'
echo '</div>'
echo '</body>'
echo '</html>'
echo ''
