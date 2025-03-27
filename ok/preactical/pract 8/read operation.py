import RPi.GPIO as gp
from mfrc522 import SimpleMFRC522
gp.setwarnings(False)
reader=SimpleMFRC522()
try:
	id,text =reader.read()
	print(id)
	print(text)
finally:
	gp.cleanup()
	
