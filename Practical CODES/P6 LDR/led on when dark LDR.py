import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


ldr_pin = 23
led_pin = 18

GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(ldr_pin,GPIO.OUT)

try:
    while True:
        ldr_value = GPIO.input(ldr_pin)
        
        if ldr_value == 0 :
            GPIO.output(led_pin,GPIO.HIGH)
        else:
            GPIO.output(led_pin,GPIO.LOW)
            
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()