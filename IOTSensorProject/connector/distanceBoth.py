import distance
import distanceRight

while True:
    distance.SensorRangeLeft()
    distanceRight.SensorRangeRight()

    #Vasemman laskeminen
    if(distance.SensorRangeLeft().distanceLeft < 50):
        if(distanceRight.SensorRangeRight().distanceRight < 50):
            print ("1")