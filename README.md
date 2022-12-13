## Hardware

This is meant to be used with my Nap Button project, so you can follow the build instructions [here](https://www.hackster.io/314reactor/the-nap-button-77cc2a).
Although it should work with pretty much any Linux system that has a speaker, some code may just need tweaking.

## Install

1. Clone this repo onto a Raspberry Pi running Raspberry Pi OS Legacy (32-bit)
2. Run the installation instructions for the Speaker pHAT [here](https://github.com/pimoroni/speaker-phat)
3. Set the program to run in ~/.bashrc (or whatever you use to run it on boot, bashrc will run it on login)
```sudo nano ~/.bashrc```
Add the following lines at the end
```sudo chmod +x ~/nap_button/boot.sh```
```~/nap_button/boot.sh```
Save the file.
4. Make the SD Card read-only, following the instructions [here](https://learn.adafruit.com/read-only-raspberry-pi)