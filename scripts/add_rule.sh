#!/bin/bash

who=$(head -n 1 user.log)
logger -t "WEBASO" "User: $who has accessed packet filtering"

read query_string

chain=$(echo "$query_string" | awk -F'&' '{split($1,a,"="); print a[2]}')
traffic_type=$(echo "$query_string" | awk -F'&' '{split($2,a,"="); print a[2]}')
action=$(echo "$query_string" | awk -F'&' '{split($3,a,"="); print a[2]}')
source_addr=$(echo "$query_string" | awk -F'&' '{split($4,a,"="); print a[2]}')
source_port=$(echo "$query_string" | awk -F'&' '{split($5,a,"="); print a[2]}')
destination_addr=$(echo "$query_string" | awk -F'&' '{split($6,a,"="); print a[2]}')
destination_port=$(echo "$query_string" | awk -F'&' '{split($7,a,"="); print a[2]}')


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
echo '</div>'
echo '  <div class="table">'
if [ -z "$chain" ] || [ -z "$traffic_type" ] || [ -z "$action" ]; then
  echo "    <div class='user_list'>"
  echo "<p>Error: Please fill in all required fields.</p>"
  echo "    </div>"
else 
    # Add the rule
    iptables_rule="iptables -A $chain -p $traffic_type"
    # Optional fields
    [ -n "$source_addr" ] && iptables_rule+=" -s $source_addr"
    [ -n "$source_port" ] && iptables_rule+=" --sport $source_port"
    [ -n "$destination_addr" ] && iptables_rule+=" -d $destination_addr"
    [ -n "$destination_port" ] && iptables_rule+=" --dport $destination_port"

eval "$iptables_rule"
iptables=$(sudo iptables -L -n -v)

echo "    <div class='user_list'>"
echo "      <pre>$iptables</pre>"
#echo "<h1>Complete iptable: $iptables_rule</h1>"
echo "    </div>"
fi
echo "</div>"
echo '</body>'
echo '</html>'
echo ''