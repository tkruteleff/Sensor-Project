import RPi.GPIO as GPIO
import time
import signal
import sys
from datetime import datetime
from DBConnector import insert

GPIO.setmode(GPIO.BCM)

#Defineing Trigger and Echo pin locations on Rasp
pinTrigger = 19
pinEcho = 13
pinRTrigger = 23
pinREcho = 24

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, close)

#Setting up the trigger and echo pin Outputs and Inputs
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
GPIO.setup(pinRTrigger, GPIO.OUT)
GPIO.setup(pinREcho, GPIO.IN)

while True:

	GPIO.output(pinTrigger, True)
	GPIO.output(pinRTrigger, True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)
	GPIO.output(pinRTrigger, False)
	time.sleep(0.00001)

	startTimeLeft = time.time()
	stopTimeLeft = time.time()

	startTimeRight = time.time()
	stopTimeRight = time.time()

	# save start time
	while 0 == GPIO.input(pinEcho):
		startTimeLeft = time.time()

	while 0 == GPIO.input(pinREcho):
		startTimeRight = time.time()

	# save time of arrival
	while 1 == GPIO.input(pinEcho):
		stopTimeLeft = time.time()

	while 1 == GPIO.input(pinREcho):
		stopTimeRight == time.time()

	# time difference between start and arrival
	TimeElapsedLeft = stopTimeLeft - startTimeLeft

	TimeElapsedRight = stopTimeRight - startTimeRight
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distanceLeft = (TimeElapsedLeft * 34300) / 2

	distanceRight = (TimeElapsedRight * 34300) / 2

	print ("Distance Left: %.1f cm" % distanceLeft)
	time.sleep(1)
	print("Distance Right: %.lf cm" % distanceRight)
	time.sleep(1)
