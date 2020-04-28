#!/bin/bash

menu=( 	"Brave|./1/browsers/brave.sh"
		"Firefox|./1/browsers/firefox.sh"
		"Vivaldi|./1/browsers/vivaldi.sh"
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
