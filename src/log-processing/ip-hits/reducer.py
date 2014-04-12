#!/usr/bin/python

import sys

hitCount = 0
prevIP = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    currentIP, currentCount = data_mapped

    if prevIP and prevIP != currentIP:
        print prevIP, "\t", hitCount
        prevIP = currentIP;
        hitCount = 0

    prevIP = currentIP
    hitCount += 1

if prevIP != None:
    print prevIP, "\t", hitCount
