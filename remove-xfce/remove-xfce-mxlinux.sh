#!/bin/bash
#It’s not totally obvious how to get rid of Xfce, so user kmathern came up with this single command:

dpkg -l | grep .xfce. | awk '{print $2}' | xargs sudo apt-get purge -V --auto-remove -yy 
dpkg -l | grep .libreoffice. | awk '{print $2}' | xargs sudo apt-get purge -V --auto-remove -yy
dpkg -l | grep .hexchat. | awk '{print $2}' | xargs sudo apt-get purge -V --auto-remove -yy
#When that has finished, then reinstall one package:

# sudo apt install desktop-defaults-mx-common

dpkg -l | grep .xed. | awk '{print $2}' | xargs sudo apt-get purge -V --auto-remove -yy
