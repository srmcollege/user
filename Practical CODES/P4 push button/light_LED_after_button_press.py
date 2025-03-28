import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


switch_pin=18         
led_pin=23

GPIO.setup(switch_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(led_pin,GPIO.OUT)

#GPIO.setwarnings(False)
led_state=False
old_input_state=True


while True:
    new_input_state=GPIO.input(switch_pin)
    if new_input_state==False and old_input_state ==True:
        print('button pushed...')
        led_state=not led_state
    old_input_state=new_input_state
    GPIO.output(led_pin,led_state)