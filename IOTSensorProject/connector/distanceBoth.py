from distance import *
from distanceRight import *
from DBConnector import insertIncrease, insertDelete

maxDistance = 90
visitorCount = 0

while True:
    if SensorRangeRight() < maxDistance:
        if SensorRangeLeft() < maxDistance:
            visitorCount = visitorCount + 1
            print (visitorCount)
            insertIncrease()
    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            visitorCount = visitorCount - 1
            print (visitorCount)
            insertDelete()
