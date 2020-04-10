#!/bin/bash

menu=( 	"Install Software-Common|sudo apt-get install software-properties-common -y"
		"Install Linux-Headers|sudo apt-get install linux-headers-$(uname -r) -y"
		"Install DKMS|sudo apt-get install dkms -y" 
		"Install GVFS|sudo apt-get install gvfs-backends -y"
		"Install Archive|sudo apt-get install xarchiver -y"
		"Install Autoconf|sudo apt-get install autoconf -y"
		"Install Git|sudo apt-get install git -y"
		"Install ADB|sudo apt-get install adb -y" 
		"Install FEH|sudo apt-get install feh -y"
		"Install Dunst|sudo apt-get install dunst -y"
		"Install Rofi|sudo apt-get install rofi -y" 
		"Install Geany|sudo apt-get install geany -y"
		"Install Geany-Plugins|sudo apt-get install geany-plugins -y" 
		"Install Alacarte|sudo apt-get install alacarte -y" 
		"Install Parole|sudo apt-get install parole -y"
		"Install wmctrl|sudo apt-get install wmctrl -y" 
		"Install Lxappearance|sudo apt-get install lxappearance -y" 
		"Install NumlockX|sudo apt-get install numlockx -y" 
		"Install Font-viewer|sudo apt-get install gnome-font-viewer -y"
		"Install Gnome-Disk|sudo apt-get install gnome-disk-utility -y"
		"Clean|sudo apt clean -y"
		"Auto-Remove|sudo apt autoremove -y"
		"Release-Upgrade|sudo do-release-upgrade -y"
		"Update-Grub|sudo grub-mkconfig -o /boot/grub/grub.cfg -y"
		"Edit-Source-List|sudo mousepad /etc/apt/sources.list -y"
		"UPDATE|sudo apt update -y" 
		"UPGRADE|sudo apt dist-upgrade -y" )

yad_opts=( --form
           --title="Miyo-Extras"
           --text="For Debian/Devuan/Ubuntu based Distros"
           --image="wall90.png"
           --align=center
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
