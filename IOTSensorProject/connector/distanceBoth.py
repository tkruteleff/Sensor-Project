from distanceRight import *
from distance import *
import Variables
import DBConnector

# If the left sensor's range is below 50cm the program checks
# if the right sensor's range is also below 50cm.
# If that is true the program lowers the visitorcount by one.
def checkLeft():
    if SensorRangeRight(dright) < Variables.maxDistance:
        if int(Variables.visitorCount) >= 0:
            Variables.visitorCount = int(Variables.visitorCount) - 1
            print (Variables.visitorCount)
            DBConnector.insertDelete()

# If the right sensor's range is below 50cm the program checks
# if the left sensor's range is also below 50cm.
# If that is true the program increases the visitorcount by one.
def checkRight():
    if SensorRangeLeft(dleft) < Variables.maxDistance:
        Variables.visitorCount = int(Variables.visitorCount) + 1
        print(Variables.visitorCount)
        DBConnector.insertIncrease()

# Calls the getLastValue method in the DBConnector.py file to check
# the previous visitorcount.
DBConnector.getLastValue()


# Checks the value of both sensors and calls the corresponding method
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
