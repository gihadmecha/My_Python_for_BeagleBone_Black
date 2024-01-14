
#imported libraries
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

#variables
redLed = "P8_11"
greenLed = "P8_12"

#initialize
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

#user inputs
blinkNo = input("Enter number of blinks: ")
delay = input("Enter delay: ")

for index in range(0, blinkNo):
           GPIO.output(redLed, GPIO.HIGH)
           GPIO.output(greenLed, GPIO.LOW)
           sleep(delay)
           GPIO.output(redLed, GPIO.LOW)
           GPIO.output(greenLed, GPIO.HIGH)
           sleep(delay)

GPIO.output (redLed, GPIO.LOW)
GPIO.output (greenLed, GPIO.LOW)
            
GPIO.cleanup()
