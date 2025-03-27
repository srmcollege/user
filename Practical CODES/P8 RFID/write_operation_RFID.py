#write operation

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

try:
    print("Place your card near the reader...")
    sleep(2)
    reader.write("Test data")
    print("Data written successfully!")
finally:
    GPIO.cleanup()
