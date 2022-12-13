cd ~/WhiteNoiseGenerator || exit
pwd
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 -y
python3 nap_button.py