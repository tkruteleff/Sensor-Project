from distance import *
from distanceRight import *
import DBConnector

maxDistance = 90
visitorCount = 0

while True:
    if SensorRangeRight() < maxDistance:
        if SensorRangeLeft() < maxDistance:
            visitorCount = visitorCount + 1
            print (visitorCount)
            DBConnector.insertIncrease()
    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            visitorCount = visitorCount - 1
            print (visitorCount)
            DBConnector.insertDelete()
