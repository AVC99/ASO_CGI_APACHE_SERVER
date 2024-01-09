#!/bin/bash
who=$(head -n 1 user.log)
logger -t "WEBASO" "User: $who has shutdown the server"

sudo shutdown -h now