#! /bin/bash

while true; do

read -p "Would you like to play rock paper scissors? (y/n): " yn

case $yn in
    [yY] ) python3 rps_game.py;
        break;;
    [nN] ) echo "That's too bad, maybe next time!";
        exit;;
    * ) echo "< invalid response >";;

esac

done

