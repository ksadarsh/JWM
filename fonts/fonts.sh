#!/bin/sh
sudo mv *.ttf /usr/share/fonts
sudo mv *.TTF /usr/share/fonts
sudo mv *.otf /usr/share/fonts
fc-cache -fv
sudo fc-cache -fv
