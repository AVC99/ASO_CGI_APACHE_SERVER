#!/bin/bash

who=$(head -n 1 user.log)
logger -t "WEBASO" "User: $who has accessed cron management"


read -r query_string

minute=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')
hour=$(echo "$query_string" | awk -F'&' '{split($2,a,"="); print a[2]}')
day_of_month=$(echo "$query_string" | awk -F'&' '{split($3,a,"="); print a[2]}')
month=$(echo "$query_string" | awk -F'&' '{split($4,a,"="); print a[2]}')
day_of_week=$(echo "$query_string" | awk -F'&' '{split($5,a,"="); print a[2]}')
command=$(echo "$query_string" | awk -F'&' '{split($6,a,"="); print a[2]}')

command=$(echo "$command" | sed 's/+/ /g')


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
fcron_command="$minute $hour $day_of_month $month $day_of_week $command"
(fcrontab -l; echo "$fcron_command") | fcrontab -

crontab=$(fcrontab -l)

echo '<div class="wrapper">'
echo '  <div class="user_tool">'
echo '    <form action="./add_cron.sh" method="post">'
echo "<i>Minute: </i>"
echo "<input type='text' name='minute' placeholder='*' value='*'/>"
echo "<i>Hour: </i>"
echo "<input type='text' name='hour' placeholder='*'  value='*'/>"
echo "<i>Day of month: </i>"
echo "<input type='text' name='day_of_month' placeholder='*' value='*'/>"
echo "<i>Month: </i>"
echo "<input type='ntext' name='month' placeholder='*' value='*'/>"
echo "<i>Day of week: </i>"
echo "<input type='text' name='day_of_week' placeholder='*'  value='*'/>"
echo "<input class='command' type='text' name='command' placeholder='Command'/>"
echo "<button type='submit''>Add task</button>"
echo "</form>"
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