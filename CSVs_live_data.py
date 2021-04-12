import csv 
import random
import time
from datetime import datetime


now = datetime.now()
testTime = 0
gps_latitude = 152.67881
number = 8

fieldnames = ["data_number", "now", "gps_latitude", "number"]

with open('./data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

while testTime != 101:#<- set the time
    with open('./data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        info = {
            'data_number': testTime,
            'now': now,
            'gps_latitude': gps_latitude,
            'number': number
        }

        csv_writer.writerow(info)
        print(testTime, now, round(gps_latitude,6), number)

        testTime += 1 #import realtime , how?
        now = datetime.now()
        gps_latitude -=  0.00002 # moving West 1 meter "{:.2f}".format(a_float)
        number = []
        for i in range(5):
            number.append(random.randint(0,16))
        number.sort()
        number = number[2]

    
    time.sleep(1)


