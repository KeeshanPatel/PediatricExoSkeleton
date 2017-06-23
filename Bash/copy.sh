#!/bin/bash

read -p 'Enter trial number you want copied: ' uservar
if [ "$uservar" -eq "0" ]
then
sudo cp -R ~/Desktop/PyScripts/DataFolder/Trial_*	~/Desktop/USB/ 
fi

if [ "$uservar" -ne "0" ]
then
sudo cp -R ~/Desktop/PyScripts/DataFolder/Trial_$uservar       ~/Desktop/USB/
fi

