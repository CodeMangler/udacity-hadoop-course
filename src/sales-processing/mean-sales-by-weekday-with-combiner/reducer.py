#!/usr/bin/python

import sys

salesTotal = 0
numberOfSales = 0

prevWeekday = None

averages = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    currentWeekday, currentSale = data_mapped

    if prevWeekday and prevWeekday != currentWeekday:
        salesAverage = (salesTotal / numberOfSales)
        averages[prevWeekday] = salesAverage
        prevWeekday = currentWeekday;
        salesTotal = 0
        numberOfSales = 0

    prevWeekday = currentWeekday
    salesTotal += float(currentSale)
    numberOfSales += 1

if prevWeekday != None:
    salesAverage = (salesTotal / numberOfSales)
    averages[prevWeekday] = salesAverage

for weekday in sorted(averages.keys()):
    print "{0}\t{1}".format(weekday, averages[weekday])
