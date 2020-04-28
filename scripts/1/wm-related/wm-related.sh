#!/bin/bash

menu=( 	"Install Alacarte|sudo apt-get install alacarte -y"
		"Install Archive|sudo apt-get install xarchiver -y"
		"Install Cbatticon|sudo apt-get install cbatticon -y"
		"Install Compton|sudo apt-get install compton -y"
		"Install Dunst|sudo apt-get install dunst -y"
		"Install DMenu|sudo apt-get install dmenu -y"		
		"Install Font-viewer|sudo apt-get install gnome-font-viewer -y"
		"Install Geany|sudo apt-get install geany -y"
		"Install Geany-Plugins|sudo apt-get install geany-plugins -y" 
		"Install Gnome-Disk|sudo apt-get install gnome-disk-utility -y"
		"Install GVFS|sudo apt-get install gvfs-backends -y"
		"Install Lxappearance|sudo apt-get install lxappearance -y"
		"Install NumlockX|sudo apt-get install numlockx -y"
		"Install Rofi|sudo apt-get install rofi -y"
		"Install VolumeIcon|sudo apt-get install volumeicon-alsa -y"
		"Install wmctrl|sudo apt-get install wmctrl -y" 
		 )

yad_opts=( --form
           --title="Miyo-Extras"
           --align=left
           --width=165
           --borders=10
           --height=250
           --columns=3
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
