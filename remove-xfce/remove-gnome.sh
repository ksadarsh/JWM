sudo apt-get remove ubuntu-gnome-desktop
sudo apt-get remove gnome-shell 

Uninstall ubuntu-gnome-desktop and it's dependencies
sudo apt-get remove --auto-remove ubuntu-gnome-desktop

sudo apt-get purge ubuntu-gnome-desktop
sudo apt-get purge --auto-remove ubuntu-gnome-desktop
sudo apt-get autoremove
sudo dpkg-reconfigure gdm
sudo apt-get remove gdm
sudo apt-get install ubuntu-desktop
sudo apt-get install unity
