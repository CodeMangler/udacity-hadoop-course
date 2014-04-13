#!/usr/bin/python

import sys

salesTotal = 0
numberOfSales = 0

prevWeekday = None

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    currentWeekday, currentSale = data_mapped

    if prevWeekday and prevWeekday != currentWeekday:
        salesAverage = (salesTotal / numberOfSales)
        print WEEKDAYS[int(prevWeekday)], "\t", salesAverage
        prevWeekday = currentWeekday;
        salesTotal = 0
        numberOfSales = 0

    prevWeekday = currentWeekday
    salesTotal += float(currentSale)
    numberOfSales += 1

if prevWeekday != None:
    salesAverage = (salesTotal / numberOfSales)
    print WEEKDAYS[int(prevWeekday)], "\t", salesAverage
