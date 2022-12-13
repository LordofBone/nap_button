## Use

This is meant to be used with my Nap Button project, so you can follow the instructions [here]().
Although it should work with pretty much any Linux system that has a speaker, some of the code may just need tweaking.

## Install

1. Clone this repo
2. Run the installation instructions for the Speaker pHAT [here](https://github.com/pimoroni/speaker-phat)
3. Install the dependencies
```pip3 install -r requirements.txt```
4. Set the program to run in rc.local (or whatever you use to run it on boot)
```sudo nano /etc/rc.local```
5. Add the following lines before the exit 0 line
```sudo chmod +x ~/nap-button/boot.sh```
```~/nap-button/boot.sh```
