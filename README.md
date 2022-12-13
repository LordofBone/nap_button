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
4. Place your sleep assisting audio into the audio folder and rename it to 'sleep_noise.mp3' (by default it is set to play this filename)
5. Configure the nap button to your liking by editing the config/nap_button_config.py file where you can change the
name of the audio file, the button pin, volume and button debounce time.
6. Make the SD Card read-only, following the instructions [here](https://learn.adafruit.com/read-only-raspberry-pi)