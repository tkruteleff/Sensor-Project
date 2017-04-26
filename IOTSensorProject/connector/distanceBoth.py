import DBConnector
import Variables

maxDistance = 90

while True:
    if Variables.distanceRightC < maxDistance:
        if Variables.distanceRightC < maxDistance:
            Variables.visitorCount = Variables.visitorCount + 1
            print (Variables.visitorCount)
            DBConnector.insertIncrease()

    elif Variables.distanceLeftC < maxDistance:
        if Variables.distanceRightC < maxDistance:
            Variables.visitorCount = Variables.visitorCount - 1
            print (Variables.visitorCount)
            DBConnector.insertDelete()
