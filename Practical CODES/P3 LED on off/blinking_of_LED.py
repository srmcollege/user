#Code For Blinking Of LED 

import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


while (True):
    GPIO.output(18 , True)
    time.sleep(0.1)
    GPIO.output(18 , False)
    time.sleep(0.9)
    print('Running')