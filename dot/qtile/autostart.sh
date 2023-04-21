#!/usr/bin/env bash
sleep 5
nitrogen --restore &
./FixMonitors.sh &
conky -c dracula-01.conkyrc &
picom --experimental-backends -b --config picom.conf &
wal -R
#redshift
#currently not working 
#picom &
