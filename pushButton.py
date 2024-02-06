
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

topButton = "P9_11"
bottomButton = "P9_13"

GPIO.setup (topButton, GPIO.IN)
GPIO.setup (bottomButton, GPIO.IN)

while (1):
	if GPIO.input (topButton):
		print "Top Button is pressed"
	if GPIO.input (bottomButton):
		print "Bottom Button is pressed"
	if GPIO.input (topButton) and GPIO.input (bottomButton):
		print "Goodbye, Come Again Soon"
		break
	sleep (.2)
GPIO.cleanup ()
