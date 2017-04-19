from distance import *
from distanceRight import *

while True:
    SensorRangeLeft()
    SensorRangeRight()

    if distanceLeftC > 50:
        print ("1")