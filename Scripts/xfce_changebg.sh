#!/bin/zsh
sed -i 's_\(^BackgroundImageFile=\)\(.*$\)_\1'"$1"'_' /home/angel/.config/xfce4/terminal/terminalrc
