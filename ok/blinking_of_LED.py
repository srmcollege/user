#Code For Blinking Of LED 

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

for i in range(0,10):
	print("Turmimng on LED")
	GPIO.output(18,True)
	time.sleep(1)
	print("Turning ofF LED")
	GPIO.output(18,False)
	time.sleep(1)
GPIO.clear()
