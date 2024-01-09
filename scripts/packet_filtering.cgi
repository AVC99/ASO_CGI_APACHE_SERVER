#!/bin/bash

who=$(head -n 1 user.log)
logger -t "WEBASO" "User: $who has accessed packet filtering"

echo 'Content-type: text/html'
echo ''
echo '<!DOCTYPE html>'
echo '<html>'
echo '<head>'
echo '<meta charset="UTF-8"/>'
echo '<title>ASO Server Home</title>'
echo '<link rel="stylesheet" href="../css/packet_filtering.css"/>'
echo '<link rel="icon" href="../icons/Hasbulla.png" type="image/png">'
echo '</head>'

echo '<body>'
echo "<header><form class='form_button'  action='./home.cgi' method='post'><button type='submit' name='user' value='$who'>Home</button></form>
<p class='title'>Packet Filtering</p>
</header>"
echo '<section>'
cat << EOF
$(for i in {1..300}; do echo "<span></span> "; done)
EOF
echo "</section>"
iptables=$(sudo iptables -L -n -v)
echo '<div class="wrapper">'
echo '  <div class="user_tool">'
echo '    <form action="./add_rule.sh" method="post">'
echo "<select name="chain" id="chain"> 
        <option value="--chain--">-- chain --</option> 
        <option value="INPUT">INPUT</option> 
        <option value="FORWARD">FORWARD</option> 
        <option value="OUTPUT">OUTPUT</option> 
    </select>"
echo "<select name="traffic-type" id="traffic-type"> 
        <option value="--traffic type--">-- traffic type --</option> 
        <option value="TCP">TCP</option> 
        <option value="UDP">UDP</option> 
        <option value="IP">IP</option> 
        <option value="ICMP">ICMP</option> 
    </select>"
echo "<select name="action" id="action"> 
        <option value="--action--">-- action --</option> 
        <option value="ACCEPT">ACCEPT</option> 
        <option value="REJECT">REJECT</option> 
        <option value="DROP">DROP</option> 
    </select>"
echo "<input type='text' name='source-address' placeholder='Source address'/>"
echo "<input type='number' name='source-port' placeholder='Source port'/>"
echo "<input type='text' name='destination-address' placeholder='Destination address'/>"
echo "<input type='number' name='destination-port' placeholder='Destination port'/>"
echo "<input type='submit' value='Add rule'/>"
echo "</form>"
echo '  </div>'
echo '  <div class="table">'
echo "    <div class='user_list'>"
echo "      <pre>$iptables</pre>"
echo "    </div>"
echo '  </div>'
echo "</div>"
echo '</body>'
echo '</html>'
echo ''