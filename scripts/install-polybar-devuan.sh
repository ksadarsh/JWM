#!/bin/sh
#Open terminal in home folder and run the script.
#My first Script for polybar installation on Debian/Ubuntu/Devuan
sudo apt update 
sudo apt upgrade -y
sudo apt-get install -y git rofi dmenu geany cmake cmake-data libcairo2-dev libxcb1-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-image0-dev libxcb-randr0-dev libxcb-util0-dev libxcb-xkb-dev pkg-config python-xcbgen xcb-proto libxcb-xrm-dev libasound2-dev libmpdclient-dev libiw-dev libcurl4-openssl-dev libpulse-dev libxcb-composite0-dev xcb libxcb-ewmh2 libxcb-ewmh-dev build-essential fonts-powerline fonts-font-awesome libxcb-keysyms1-dev libxcb-xinerama0-dev python3-sphinx libxcb-cursor-dev libjsoncpp-dev libnl-genl-3-dev -y
git clone --branch 3.4 --recursive https://github.com/jaagr/polybar
cd polybar
sh build.sh
sudo apt update
