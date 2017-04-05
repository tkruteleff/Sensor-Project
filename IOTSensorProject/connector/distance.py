import RPi.GPIO as GPIO
import time
import signal
import sys
from datetime import datetime
from DBConnector import insert

GPIO.setmode(GPIO.BCM)

pinTrigger = 19
pinEcho = 13

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, close)

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:

	GPIO.output(pinTrigger, True)
	
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

	startTime = time.time()
	stopTime = time.time()

	# save start time
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	# save time of arrival
	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	if distance < 10:
		print("1")
		insert()
		print(str(datetime.now()))
	
	print ("Distance: %.1f cm" % distance)
	time.sleep(1)
