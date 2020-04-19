#!/bin/bash

menu=( 	"Install ADB|sudo apt-get install adb -y"
		"Install Alacarte|sudo apt-get install alacarte -y"
		"Install Archive|sudo apt-get install xarchiver -y"
		"Install Autoconf|sudo apt-get install autoconf -y"
		"Install Cbatticon|sudo apt-get install cbatticon -y"
		"Install Compton|sudo apt-get install compton -y"
		"Install CURL|sudo apt-get install curl -y"
		"Install DKMS|sudo apt-get install dkms -y"
		"Install Dunst|sudo apt-get install dunst -y"
		"Install DMenu|sudo apt-get install dmenu -y"
		"Install FEH|sudo apt-get install feh -y"
		"Install Firefox|sudo apt install firefox -yy"
		"Install Font-viewer|sudo apt-get install gnome-font-viewer -y"
		"Install Geany|sudo apt-get install geany -y"
		"Install Geany-Plugins|sudo apt-get install geany-plugins -y" 
		"Install Gimp|sudo apt install gimp -yy"
		"Install Git|sudo apt-get install git -y"
		"Install Gnome-Disk|sudo apt-get install gnome-disk-utility -y"
		"Install GVFS|sudo apt-get install gvfs-backends -y"
		"Install Inkscape|sudo apt install inkscape -yy"
		"Install Linux-Headers|sudo apt-get install linux-headers-$(uname -r) -y"
		"Install Lxappearance|sudo apt-get install lxappearance -y"
		"Install NumlockX|sudo apt-get install numlockx -y"
		"Install Parole|sudo apt-get install parole -y"
		"Install Rofi|sudo apt-get install rofi -y"
		"Install Software-Common|sudo apt-get install software-properties-common -y"
		"Install VolumeIcon|sudo apt-get install volumeicon-alsa -y"
		"Install wmctrl|sudo apt-get install wmctrl -y" 
		"Install WGET|sudo apt-get install wget -y"
		"Auto-Remove|sudo apt autoremove -y"
		"Clean|sudo apt clean -y"
		"Edit-Source-List|sudo geany /etc/apt/sources.list -y"
		"Release-Upgrade|sudo do-release-upgrade -y"
		"Surfn-Icons|./icons-surfn-v4.sh"
		"Terminal&Editors|./101-terminals-apps-editors.sh"
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
