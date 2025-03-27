#Code For Only LED Lighting 

import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

GPIO.output(27 , True)