#!/bin/sh
# save this as a file and make executable

# detect monitor
MON=$(xrandr -q | grep " connected" | cut -f1 -d ' ')

# find current xrandr brightness value
XR=$(xrandr --verbose | grep -i brightness | cut -f2 -d ' ' | head -n1)
BrCur=`awk "BEGIN {print $XR*100}"` # calculate, so e.g. 0.5 gets 50
BrMax="100"

# Set scale minimum here
BrMin="5"

# Set step here for keyboard left/right and mouse scroll
Step="5"

# yad scale dialog
yad --scale  --step $Step --mouse --skip-taskbar --min-value $BrMin --max-value $BrMax \
    --value $BrCur --print-partial --undecorated --width 300 \
    --on-top --escape-ok --no-buttons --hide-value --close-on-unfocus \
| while read BrNew; do
    # division using awk, so xrandr value gets e.g. 0.5 rather than 50
    xrandr --output $MON --brightness $(awk "BEGIN {print $BrNew/100}")
done
