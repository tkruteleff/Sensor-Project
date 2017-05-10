from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    if distanceRightC < Variables.maxDistance:
            if distanceLeftC < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif distanceLeftC < Variables.maxDistance:
        if distanceRightC < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
