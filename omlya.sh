#!/bin/bash

for i in `seq 1 25`; do
  xdotool mousemove 2947 840 click 1
  xdotool mousemove 2737 811 click 1
  xdotool key o m l y a a a a a a a Return
  sleep 0.001
done
