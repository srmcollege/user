import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.output(17 , False)
GPIO.output(18 , False)
GPIO.output(27 , False)

while (True):
    GPIO.output(17 , True)
    time.sleep(0.1)
    GPIO.output(17 , False)
    time.sleep(0.1)
    GPIO.output(18 , True)
    time.sleep(0.1)
    GPIO.output(18 , False)
    time.sleep(0.1)
    GPIO.output(27 , True)
    time.sleep(0.1)
    GPIO.output(27 , False)
    print('Running')
