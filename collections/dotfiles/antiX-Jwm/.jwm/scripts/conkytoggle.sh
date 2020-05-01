#!/bin/bash
# Filename:      conkytoggleflux.sh
# Purpose:       toggle conky on/off from fluxbox menu
# Authors:       Kerry and anticapitalista, secipolla for antiX
# Latest change: Wed March 24, 2010.
################################################################################

if pidof conky | grep [0-9] > /dev/null
 then
  killall conky 
 else
  conky 
fi
