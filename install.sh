echo "Installing..."
sudo apt-get install python3-dev python3-pip
sudo pip3 install rpi
sudo apt-get install python3-rpi.gpio
sudo python3 -m pip install mfrc52
sudo pip3 install spotify-cli
echo "Please authorize spotify"
spotify auth login
echo "Thanks! The program is now installed."