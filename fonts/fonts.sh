#!/bin/sh
sudo cp -rf *.ttf /usr/share/fonts
sudo cp -rf *.otf /usr/share/fonts
fc-cache -fv
sudo fc-cache -fv
