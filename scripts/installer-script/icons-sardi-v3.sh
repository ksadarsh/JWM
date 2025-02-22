#!/bin/bash
#
##################################################################################################################
# Written to be used on 64 bits computers
# Author 	: 	Erik Dubois
# Website 	: 	http://www.erikdubois.be
##################################################################################################################
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################


# cleaning tmp
[ -d /tmp/sardi ] && rm -rf /tmp/sardi

# if there is no hidden folder then make one
[ -d $HOME"/.icons" ] || mkdir -p $HOME"/.icons"

wget -O /tmp/sardi.tar.gz "https://sourceforge.net/projects/sardi/files/latest/download?source=files"
mkdir /tmp/sardi
tar -zxf /tmp/sardi.tar.gz -C /tmp/sardi
rm /tmp/sardi.tar.gz
sudo cp -rf /home/adarsh/Downloads/sardi/* /usr/share/icons/
tar -zxf sardi-icons-20.4-1.tar.gz -C /home/adarsh/Downloads/sardi/
# cleaning tmp
[ -d /tmp/sardi ] && rm -rf /tmp/sardi



echo "################################################################"
echo "###################    icons sardi done   ######################"
echo "################################################################"
