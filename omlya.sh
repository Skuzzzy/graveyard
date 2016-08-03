#!/bin/bash

for i in `seq 1 100000`; do
  xdotool mousemove 2947 882 click 1
  xdotool mousemove 2737 811 click 1
  xdotool key o m l y a a a a a a a Return
  sleep 2
done
