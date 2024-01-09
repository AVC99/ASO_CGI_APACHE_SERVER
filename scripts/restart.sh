#!/bin/bash
who=$(head -n 1 user.log)
logger -t "WEBASO" "User: $who has restarted the server"

sudo reboot