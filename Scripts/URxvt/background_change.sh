#!/bin/zsh
sed -i 's_\([^\/]*\)\(;style=centered$\)_'"$1"'\2_' /home/angel/.Xresources
xrdb ~/.Xresources
