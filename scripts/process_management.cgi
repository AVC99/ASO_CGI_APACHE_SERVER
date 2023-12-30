#!/bin/bash

who=$(head -n 1 user.log)
echo -e "User: $who has entered the process management page" >> ./register.log

echo 'Content-type: text/html'
echo ''
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/process_management.css"/>'
echo '<link rel="icon" href="../icons/Hasbulla.png" type="image/png">'
echo '</head>'

echo '<body>'

echo "<header><form class='form_button'  action='./home.cgi' method='post'><button type='submit' name='user' value='$who'>Home</button></form>
<p class='title'>Process Management</p>
</header>"
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo "</section>"
ps_aux=$(ps aux | awk '{print $1" "$2" "$8" "$11}')
echo '<div class="wrapper">'
echo '  <div class="user_tool">'
echo '    <form action="./interrupt_pid.sh" method="post">'
echo '      <input type="number" name="pid" id="pid" placeholder="PID" required/>'
echo '      <input type="number" name="seconds" id="seconds" placeholder="seconds" required/>'
echo '      <button type="submit" name="interrupt">Interrupt</button>'
echo '    </form>'
echo '    <form action="./kill_pid.sh" method="post">'
echo '      <input type="number" name="pid" id="pid" placeholder="PID" required/>'
echo '      <button type="submit" name="kill">Kill</button>'
echo '    </form>'
echo '  </div>'
echo '  <div class="table">'
echo "    <div class='pids_list'>"
echo "      <pre>$ps_aux</pre>"
echo "    </div>"
echo '  </div>'
echo "</div>"

echo '</body>'
echo '</html>'
echo ''