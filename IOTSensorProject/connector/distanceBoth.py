from distance import *
from distanceRight import *
from DBConnector import *
import time

localtime = time.asctime(time.localtime(time.time()))
maxDistance = 90

print(localtime)

while True:
    if SensorRangeRight() < maxDistance:
        if SensorRangeLeft() < maxDistance:
            print ("1")
            # insert1()
    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            print("2")
            # insert2()