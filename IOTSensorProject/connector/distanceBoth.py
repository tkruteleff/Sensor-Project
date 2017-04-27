from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    SensorRangeLeft(), SensorRangeRight()

    if SensorRangeRight().str("distanceRightC") < Variables.maxDistance:
            if SensorRangeLeft().str("distanceLeftC") < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft().str("distanceLeftC") < Variables.maxDistance:
        if SensorRangeRight().str("distanceRightC") < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
