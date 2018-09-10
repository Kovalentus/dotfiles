#!/bin/bash

xfce4-terminal -e ncmpcpp &
sleep 0.1
xfce4-terminal -e vis &
i3-msg layout toggle split
sleep 0.1
i3-msg focus up
