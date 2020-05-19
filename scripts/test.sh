#!/bin/bash

menu=( "Install Rofi|sudo apt-get install rofi -y" "Install Geany|sudo apt-get install geany -y"
       "Install YAD|sudo apt-get install yad -y"   "Install Parole|sudo apt-get install parole -y"
       "Install wmctrl|sudo apt-get install wmctrl -y" "Install ADB|sudo apt-get install adb -y"
       "Install FEH|sudo apt-get install feh -y" "Install Dunst|sudo apt-get install dunst -y"
       "Install Lxappearance|sudo apt-get install lxappearance -y" "Install Autoconf|sudo apt-get install autoconf -y"
       "Install NumlockX|sudo apt-get install numlockx -y" "Install Git|sudo apt-get install git -y"
       "UPDATE|sudo apt update -y && sudo apt dist-upgrade -y" )

yad_opts=( --form
           --title="Miyo-Extras"
           --text="Select Here"
           --image="wall89.png"
           --align=left
           --width=165
           --borders=10
           --height=200
           --columns=4
           --button="Install" --button="Exit" )

for m in "${menu[@]}"
do
  yad_opts+=( --field="${m%|*}:CHK" )
done

IFS='|' read -ra ans < <( yad "${yad_opts[@]}" )

for i in "${!ans[@]}"
do
  if [[ ${ans[$i]} == TRUE ]]
  then
    m=${menu[$i]}
    name=${m%|*}
    cmd=${m#*|}
    echo "selected: $name ($cmd)"
    $cmd
  fi
done
exit 0
