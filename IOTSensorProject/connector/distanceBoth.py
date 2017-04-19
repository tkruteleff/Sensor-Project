from distance import *
left = __import__(SensorRangeLeft()).distance.distanceLeftC
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight()

    if (left > 50):
        print ("1")