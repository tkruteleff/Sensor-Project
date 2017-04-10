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

	startTime = time.time()
	stopTime = time.time()

	# save start time
	while 0 == GPIO.input(pinEcho) & 0 == GPIO.input(pinREcho):
		startTime = time.time()

	# save time of arrival
	while 1 == GPIO.input(pinEcho) & 1 == GPIO.input(pinREcho):
		stopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	print ("Distance: %.1f cm" % distance)
	time.sleep(1)
