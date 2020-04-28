#!/bin/sh
sudo apt install virtualbox virtualbox-ext-pack -yy
sudo usermod -aG vboxusers $USER
sudo chown $USER /etc/environment
sudo chmod 755 /etc/environment
