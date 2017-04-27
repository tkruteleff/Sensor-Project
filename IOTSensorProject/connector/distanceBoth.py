from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    SensorRangeLeft(), SensorRangeRight()

    if SensorRangeRight().distanceRightC < Variables.maxDistance:
            if SensorRangeLeft().distanceLeftC < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft().distanceLeftC < Variables.maxDistance:
        if SensorRangeRight().distanceRightC < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
