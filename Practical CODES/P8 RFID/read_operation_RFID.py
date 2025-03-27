#read operation

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False) 

reader = SimpleMFRC522()

try:
    data_to_write = "Blue card......"
    print("Place your card near the reader to erite data..")
    reader.write(data_to_write)
    print("Data writen to card sucessfully")
finally:
    GPIO.cleanup()
    
    
   