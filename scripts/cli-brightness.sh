#!/bin/bash
# vb -- v0.1 - Video/Display Brightness -- 02.05.2019
# ====================================================
# # SolydXee XFCE x64

# the CLI command: xrandr -q |grep " connected"
# -- should return the ID of displays currently
#    active on your system.
# ----------------------------------------------------
# !! NOTE: NOT advised TO EXCEED "1.0" setting !!

# *** Variables (start) ******************************
# ****************************************************
DISPLAYS="2"                      # Connected Displays
#
DISPLAY1="HDMI-1"                 # ID: Display 1
DISPLAY2="HDMI-2"                 # ID: Display 2
#
SETMSG="Display(s) adjusted to: "

# *****************************************************
# *** Variables (end)**********************************

clear

echo; echo "  ===== vb v0.1--02.03.2019 ====="; echo

# .....................................................
# ... Check for Varible presence and Range ............
# .....................................................

# --- is CLI variable present? ------------------------

if [[ $1 = "" ]]; then
  echo "  !! CLI Variable is missing !!";echo;
  echo "    -- usage: vb 1  (values 0-9 supported)";echo;
  exit
fi

# --- is CLI variable  0 to 9? ------------------------

# !! Both ZERO & ONE trigger 100% brightness !!

if [[ $1 = [0-9] ]]; then

#  --- CLI meets all criteria - proceed ---------------

  case "$1" in
    0) echo "    "$SETMSG"1.0";echo;
       xrandr --output $DISPLAY1 --brightness 1.0
       xrandr --output $DISPLAY2 --brightness 1.0
       ;;
    9) echo "    "$SETMSG"0.9";echo;
       xrandr --output $DISPLAY1 --brightness 0.9
       xrandr --output $DISPLAY2 --brightness 0.9
       ;;
    8) echo "    "$SETMSG"0.8";echo;
       xrandr --output $DISPLAY1 --brightness 0.8
       xrandr --output $DISPLAY2 --brightness 0.8
       ;;
    7) echo "    "$SETMSG"0.7";echo;
       xrandr --output $DISPLAY1 --brightness 0.7
       xrandr --output $DISPLAY2 --brightness 0.7
       ;;
    6) echo "    "$SETMSG"0.6";echo;
       xrandr --output $DISPLAY1 --brightness 0.6
       xrandr --output $DISPLAY2 --brightness 0.6
       ;;
    5) echo "    "$SETMSG"0.5";echo;
       xrandr --output $DISPLAY1 --brightness 0.5
       xrandr --output $DISPLAY2 --brightness 0.5
       ;;

    4) echo "    "$SETMSG"0.4";echo;
       xrandr --output $DISPLAY1 --brightness 0.4
       xrandr --output $DISPLAY2 --brightness 0.4
       ;;

# !!! Values 2 3 are ENABLED - Commands are DISABLED/NOT Tested !!!
#     -- Test carefully -- so you don't "fade to black" and possibly loose work!

    3) echo "    "$SETMSG"0.3";echo;
       #xrandr --output $DISPLAY1 --brightness 0.3
       #xrandr --output $DISPLAY2 --brightness 0.3
       ;;
    2) echo "    "$SETMSG"0.2";echo;
       #xrandr --output $DISPLAY1 --brightness 0.2
       #xrandr --output $DISPLAY2 --brightness 0.2
       ;;
    1) echo "    "$SETMSG"1.0";echo;
       xrandr --output $DISPLAY1 --brightness 1.0
       xrandr --output $DISPLAY2 --brightness 1.0
       ;;
   esac
else
  echo "  !! CLI Value is NOT supported !!";echo;
  echo "    -- usage: vb 1  (values 0-9 supported)";echo;
  exit
fi

exit
