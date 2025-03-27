import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


while (True):
    GPIO.output(18, False)
    time.sleep(2)
    GPIO.output(18, True)
    time.sleep(2)

    print('Running')
