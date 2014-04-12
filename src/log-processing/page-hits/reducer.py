#!/usr/bin/python

import sys

hitCount = 0
prevPage = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    currentPage, currentCount = data_mapped

    if prevPage and prevPage != currentPage:
        print prevPage, "\t", hitCount
        prevPage = currentPage;
        hitCount = 0

    prevPage = currentPage
    hitCount += 1

if prevPage != None:
    print prevPage, "\t", hitCount
