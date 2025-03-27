import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()
try:
	text=input("enter the data : ")
	print("place the card ")
	reader.write(text)
	print("written successflly")
finally:
	GPIO.cleanup()
