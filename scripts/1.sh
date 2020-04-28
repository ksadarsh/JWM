#!/bin/bash

menu=( 	"Install Git & Related|sudo apt-get install git wget curl cmake autoconf software-properties-common -y"
		"Install yad|sudo apt-get install yad -y"
		"Android-Related|./1/android/android.sh"
		"Icons|./1/icons/icons.sh" 
		"Installers|./1/installers/installers.sh"
		"Multimedia|./1/multimedia/multimedia.sh"
		"Browsers|./1/browsers/browsers.sh"
		"Image Editors|./1/image-editors/image-editors.sh"
		"Image Window-Manager Related|./1/wm-related/wm-related.sh"
		"Image Editors|./1/image-editors/image-editors.sh"
		"Virtualbox-Related|./1/virtualbox/virtualbox.sh"
		"Install ZSH|./1/zsh/zsh.sh")

yad_opts=( --form
           --title="Miyo-Extras-Main"
           --align=left
           --width=165
           --borders=10
           --height=250
           --columns=1
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
