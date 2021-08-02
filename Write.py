#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	print("PLease use a spotify URI! https://support.symdistro.com/hc/en-us/articles/360039036711-Spotify-How-to-obtain-a-URI-URL ")
        text = input('URI: ')
        print("Now place your tag to write")
        reader.write(text)
        print("Written '" + text + "' to tag!")
finally:
        GPIO.cleanup()
