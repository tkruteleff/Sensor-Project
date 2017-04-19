from distance import *
from distanceRight import *

maxRange = 90
minRange = 10

left = distanceLeftC
right = distanceRightC

while True:
    SensorRangeLeft()
    SensorRangeRight()

    if left > minRange & left < maxRange:
        print ("1")
    if right > minRange & right < maxRange:
        print ("2")