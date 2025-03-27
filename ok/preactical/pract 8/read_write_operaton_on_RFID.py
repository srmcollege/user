#sudo raspi-config  (choose 3rd option then enter and chose 4th option and enter)
#Sudo reboot
#Sudo apt update
#Sudo apt install python3-spidev
#Git clone https://github.com/pimylifeup/MFRC522-python.git
#cd MFRC522-python
#Sudo python3 setup.py install

#3.3v/vcc pin1
#RST pin 22
#GND pin 6
#MISO pin 21
#MOSI pin 19
#SCK pin 23
#SDA pin 24

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

