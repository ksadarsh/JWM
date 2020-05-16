#!/bin/sh

if [ "$1" = "-h" ]
then
  echo "Usage: $0 [LOCATION | -h | --help]"
  echo "Installs pmenu to the given location."
  echo ""
  echo " -h, --help   Shows this message."
  echo ""
  echo "With no LOCATION specified, it installs in the HOME directory"
  echo "(~/bin, ~/.local/share/applications). Otherwise, LOCATION should"
  echo "probably be /usr/local or /usr, in which case you need to run"
  echo "this script as root."
  exit 0
fi

# Echo on
set -e
# Crash on errors
set -x

if [ $# -eq 0 ]
then
  mkdir ~/bin 2>/dev/null || true
  install -t ~/bin pmenu.py
  mkdir -p ~/.local/share/applications 2>/dev/null || true
  install -t ~/.local/share/applications pmenu.desktop
else
  install -t "$1/bin" pmenu.py
  install -t "$1/share/applications" pmenu.desktop
fi
