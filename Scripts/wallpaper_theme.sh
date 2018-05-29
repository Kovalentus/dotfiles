#!/usr/bin/env sh
wal -g -i "$1"
wal-steam -w
feh --bg-scale "$1"
