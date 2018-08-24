#!/bin/zsh

# rxvt -e /usr/local/bin/pipes.sh -p 3 -r 5000 -s 10 &
rxvt -e cmatrix &
sleep 0.1
i3-msg fullscreen
i3lock -c '#1b283c' -o '#191d0f' -w '#572020' -l '#F5F5F5' -n; i3-msg kill
# i3lock -i $HOME/Pictures/Mountains.png  -c '#000000' -o '#191d0f' -w '#572020' -l '#F5F5F5' -n; i3-msg kill
#273a57
