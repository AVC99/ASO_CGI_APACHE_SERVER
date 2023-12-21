#!/bin/bash

echo 'Content-type: text/html'
echo ''
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8" />'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/home.css" />'
echo '</head>'
echo '<body>'
who=$(whoami)
echo "<header> Welcome $who </header>"
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo '<div class="signin">'
echo '<div class="content">'
echo '<h2>HOME</h2>'
echo '</div>'
echo '</div>'
echo '</body>'
echo '</html>'
echo ''
