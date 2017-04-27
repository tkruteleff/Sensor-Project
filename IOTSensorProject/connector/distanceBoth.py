from distanceRight import *
from distance import *
import Variables
import DBConnector


while True:
    if SensorRangeRight() < maxDistance:
            if SensorRangeLeft() < maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            if Variables.visitorCount >= 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
