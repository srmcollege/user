import RPi.GPIO as GPIO
import time

# Set GPIO mode and suppress warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pin for the LED
LED_PIN = 14

# Set up the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Define the GPIO pin for the LDR
LDR_PIN = 18

# Set up the LDR pin as an input
GPIO.setup(LDR_PIN, GPIO.IN)

def is_dark():
    # Read the LDR value (0 or 1)
    ldr_value = GPIO.input(LDR_PIN)
    return ldr_value == 0  # LDR value of 0 indicates darkness

try:
    while True:
        if is_dark():
            # Turn the LED on
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Dark: LED ON")
        else:
            # Turn the LED off
            GPIO.output(LED_PIN, GPIO.LOW)
            print("Light: LED OFF")
        time.sleep(1)  # Check LDR every second

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()
