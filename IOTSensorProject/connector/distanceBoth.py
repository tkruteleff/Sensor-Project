from distance import *
from distanceRight import *
from DBConnector import *

maxDistance = 90
visitorCount = 0

while True:
    if SensorRangeRight() < maxDistance:
        if SensorRangeLeft() < maxDistance:
            print ("1")
            visitorCount = visitorCount + 1
            # insert1()
            print (visitorCount)
    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            print("2")
            visitorCount = visitorCount - 1
            # insert2()
            print (visitorCount)