from distance import *
from distanceRight import *
from DBConnector import *

maxDistance = 90


while True:
    if SensorRangeRight() < maxDistance:
        if SensorRangeLeft() < maxDistance:
            print ("1")
            # insert1()
    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            print("2")
            # insert2()
