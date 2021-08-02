#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print("card id: " + id)
        print("card data: " + text)
        os.system("spotify play --uri " + text)
finally:
        GPIO.cleanup()
