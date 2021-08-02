read -p "Would you like to read or write info? (r/w): " readwrite
if [ $readwrite =  "w" ]
then
    sudo python3 Write.py
fi
if [ $readwrite = "r" ]
then
    sudo python3 Read.py
fi
