from distanceRight import *
from distance import *
import Variables
import DBConnector


def checkLeft():
    if SensorRangeRight(dright) < Variables.maxDistance:
        if Variables.visitorCount >= 0:
            Variables.visitorCount += Variables.visitorCount
            print (Variables.visitorCount)
            DBConnector.insertDelete()


def checkRight():
    if SensorRangeLeft(dleft) < Variables.maxDistance:
        Variables.visitorCount += Variables.visitorCount
        print(Variables.visitorCount)
        DBConnector.insertIncrease()


while True:

    if SensorRangeLeft(dleft) < Variables.maxDistance:
        checkLeft()
        # if SensorRangeRight(dright) < Variables.maxDistance:
        #   Variables.visitorCount = Variables.visitorCount + 1
        ## DBConnector.insertIncrease()

    if SensorRangeRight(dright) < Variables.maxDistance:
        checkRight()
        # if SensorRangeLeft(dleft) < Variables.maxDistance:
        #   if Variables.visitorCount > 0:
        #      Variables.visitorCount = Variables.visitorCount - 1
        ##    DBConnector.insertDelete()
