#!/bin/bash

menu=( 	"Install DKMS|sudo apt-get install dkms -y"
		"Install Linux-Headers|sudo apt-get install linux-headers-$(uname -r) -y"
		"Auto-Remove|sudo apt autoremove -y"
		"Clean|sudo apt clean -y"
		"Edit-Source-List|sudo geany /etc/apt/sources.list -y"
		"Release-Upgrade|sudo do-release-upgrade -y"
		"Copy-Fonts|/home/adarsh/JWM/fonts/fonts.sh"
		"Update-Grub|sudo grub-mkconfig -o /boot/grub/grub.cfg -y"
		"UPDATE|sudo apt update -y" 
		"UPGRADE|sudo apt dist-upgrade -y" )

yad_opts=( --form
           --title="Miyo-Extras"
           --image="jwm-white.png"
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
