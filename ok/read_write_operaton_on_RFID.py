#Read and write operation in RFID 

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

try:
    data_to_write = "Blue card......"
    print("Place your card near the reader to write data..")
    reader.write(data_to_write)
    print("Data written to card successfully")

    sleep(2)
    print("\nNow place your card near the reader to read data...")

    id, text = reader.read()
    print(f"\nCard ID: {id}")
    print(f"Card Data: {text.strip()}")

finally:
    GPIO.cleanup()
    print("\nGPIO cleanup done. Exiting program.")

