import RPi.GPIO as GPIO
import time
GPIO.cleanup()
sensor=16
buzzer=31 
motor=22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(motor,GPIO.OUT)
GPIO.output(motor,False)
print('IR sensor Ready')
print('')
try:
	while True:
		buzzer=31
		GPIO.setup(buzzer,GPIO.OUT) 
		GPIO.output(buzzer,True) 
		if GPIO.input(sensor):
			start_time=time.time()
			while GPIO.input(sensor):
				time.sleep(0.2)
				elapsed_time=time.time()-start_time
				if elapsed_time>=1.5:
					GPIO.output(buzzer,False)
					print('Object detected more than 2 seconds')
					GPIO.output(motor,True)
				else:
					GPIO.output(buzzer,True)
		else:
			GPIO.output(buzzer,True)
			GPIO.output(motor,False)
			GPIO.cleanup(buzzer)
except KeyboardInterrupt:
	GPIO.cleanup()
