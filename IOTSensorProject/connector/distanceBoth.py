from distanceRight import *
from distance import *
import Variables
import DBConnector


while True:
    if SensorRangeRight() < maxDistance:
            if SensorRangeLeft() < maxDistance:
                visitorCount = Variables.visitorCount + 1
                print (visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            visitorCount = Variables.visitorCount - 1
            print (visitorCount)
            DBConnector.insertDelete()
