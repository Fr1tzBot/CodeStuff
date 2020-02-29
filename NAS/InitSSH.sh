#!/usr/bin/expect -f
spawn ssh user@hostname
expect "password:"
sleep 1
send "<your password>\r"