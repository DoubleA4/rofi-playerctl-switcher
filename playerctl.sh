#!/bin/bash

PLAYER=`cat ~/.config/i3/scripts/player`

echo "playerctl -p $PLAYER $1"
playerctl -p $PLAYER $1