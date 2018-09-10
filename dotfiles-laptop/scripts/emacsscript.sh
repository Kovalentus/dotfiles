#!/bin/zsh

if pgrep -x "emacs" > /dev/null
then
    exec emacsclient -c
else
    exec emacs
fi
