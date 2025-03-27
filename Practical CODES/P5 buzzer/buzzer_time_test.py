import RPi.GPIO as GPIO
import time
buzzer_pin= 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer_pin,GPIO.OUT)

def buzz(pitch,duration):
    period=1.0
    delay=period/2
    cycle=int(pitch*duration)
    for i in range(cycle):
        GPIO.output(buzzer_pin,True)
        time.sleep(delay)
        GPIO.output(buzzer_pin,False)
        time.sleep(delay)
while True:
    pitch_s=input("enter the pitch(200 to 2000):")
    pitch=float(pitch_s)
    duration_s=input("enter the duration(Seconds): ")
    duration=float(duration_s)
    buzz(pitch,duration)