import distance
import distanceRight

while True:
    distance.SensorRangeLeft()
    distanceRight.SensorRangeRight()

    #Vasemman laskeminen
    if distance.SensorRangeLeft < 50:
        print("1")