from distanceRight import *
from distance import *
import Variables
import DBConnector


while True:
    if SensorRangeRight() < Variables.maxDistance:
            if SensorRangeLeft() < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft() < Variables.maxDistance:
        if SensorRangeRight() < Variables.maxDistance:
            Variables.visitorCount = Variables.visitorCount - 1
            print (Variables.visitorCount)
            DBConnector.insertDelete()
