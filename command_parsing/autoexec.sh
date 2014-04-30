#!/bin/bash
while :
do
        echo "Starting.."
        cd /home/pi/airwellhvac/command_parsing
        python ir_comms.py
        echo "re-starting.."
        sleep 10
done

###
# @reboot /usr/bin/byobu-screen -fa -d -m -S airwell /home/pi/airwellhvac/command_parsing/autoexec.sh
#