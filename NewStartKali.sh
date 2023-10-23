#!/bin/bash

echo "welcome to the installer, We're about to install some good shit for you" 
sleep 1

echo
echo "First lets get some package updates"
sudo apt update

echo
echo "Installing threader3000"
sudo pip3 install threader3000
echo "threader3000 installed"
sleep .5

echo
echo "Installing dirsearch...."
sudo apt install dirsearch
egoChorizo/Manual.gitecho "dirsearch installed"
sleep .5

echo
echo "Installing terminator"
sudo apt install terminator
echo "TERMINATOR INSTALLED"

echo
echo "CLEANING STUFF UP NOW"
sudo apt autoremove

echo
echo "GOOD TO GO, HAPPY HUNTING!"
