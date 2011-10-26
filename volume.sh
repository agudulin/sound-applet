#!/bin/bash

current=`amixer -c 0 sget "Master Front" | grep Front\ Left: | cut -b 24-25`
echo $current
if [ "x$1" = "xup" ]; then
    current=$(($current +1))
    amixer -c 0 sset "Master Front" $current
    echo $current>/tmp/currentvolume
    
else if [ "x$1" = "xdown" ]; then
    if [ $current -gt 0 ]; then
        current=$(($current -1))
        amixer -c 0 sset "Master Front" $current
        echo $current>/tmp/currentvolume
    fi
else if [ "x$1" = "xmute" ]; then
    if [ $current -eq 0 ]; then
        if [ -e /tmp/volume ]; then
            current=`cat /tmp/volume`
            amixer -c 0 sset "Master Front" $current
            rm /tmp/volume
        fi
    else
        amixer -c 0 sset "Master Front" 0
        echo $current>/tmp/volume
        current=0
    fi
fi;fi;fi
mplayer /usr/share/sounds/ubuntu/stereo/bell.ogg
