#!/bin/zsh

if pgrep -x "emacs-snapshot" > /dev/null
then
    exec emacsclient-snapshot -c
else
    exec emacs-snapshot
fi
