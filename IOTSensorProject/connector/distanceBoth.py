import distance
import distanceRight
from threading import Thread

t1 = Thread(target = distance.SensorRangeLeft())
t2 = Thread(target = distanceRight.SensorRangeRight())

t1.start()
t2.start()
t1.join()
t2.join()
