#!/bin/bash

who=$(head -n 1 user.log)
logger -t "WEBASO" "User: $who has accessed cron management"

crontab=$(fcrontab -l)

echo 'Content-type: text/html'
echo ''
echo '<!DOCTYPE html>'
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/cron_management.css"/>'
echo '<link rel="icon" href="../icons/Hasbulla.png" type="image/png">'
echo '</head>'

echo '<body>'
echo "<header><form class='form_button'  action='./home.cgi' method='post'><button type='submit' name='user' value='$who'>Home</button></form>
<p class='title'>Cron Management</p>
</header>"
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo "</section>"
echo '<div class="wrapper">'
echo '  <div class="user_tool">'
echo '  <div class="cron_line">'
echo '    <form action="./add_cron.sh" method="post">'
echo "        <i>Minute: </i>"
echo "        <input type='text' name='minute' placeholder='*' value='*'/>"
echo "        <i>Hour: </i>"
echo "        <input type='text' name='hour' placeholder='*'  value='*'/>"
echo "        <i>Day of month: </i>"
echo "        <input type='text' name='day_of_month' placeholder='*' value='*'/>"
echo "        <i>Month: </i>"
echo "        <input type='text' name='month' placeholder='*' value='*'/>"
echo "        <i>Day of week: </i>"
echo "        <input type='text' name='day_of_week' placeholder='*'  value='*'/>"
echo "        <input class='command' type='text' name='command' placeholder='Command'/>"
echo "        <button type='submit'>Add task</button>"
echo "     </form>"
echo "  </div>"
echo '  <div class="cron_line">'
echo '    <form action="./remove_cron.sh" method="post">'
echo "<i>Minute: </i>"
echo "<input type='text' name='minute' placeholder='*' value='*'/>"
echo "<i>Hour: </i>"
echo "<input type='text' name='hour' placeholder='*'  value='*'/>"
echo "<i>Day of month: </i>"
echo "<input type='text' name='day_of_month' placeholder='*' value='*'/>"
echo "<i>Month: </i>"
echo "<input type='text' name='month' placeholder='*' value='*'/>"
echo "<i>Day of week: </i>"
echo "<input type='text' name='day_of_week' placeholder='*'  value='*'/>"
echo "<input class='command' type='text' name='command' placeholder='Command'/>"
echo "<button type='submit'>Remove task</button>"
echo "</form>"
echo "</div>"
echo '  </div>'
echo '  <div class="table">'
echo "    <div class='user_list'>"
echo "      <pre>$crontab</pre>"
echo "    </div>"
echo '  </div>'
echo "</div>"
echo '</body>'
echo '</html>'
echo ''