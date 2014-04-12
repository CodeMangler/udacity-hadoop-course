#!/usr/bin/python

import sys

itemTotal = 0
oldItem = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisItem, thisSale = data_mapped

    if oldItem and oldItem != thisItem:
        print oldItem, "\t", itemTotal
        oldItem = thisItem;
        itemTotal = 0

    oldItem = thisItem
    itemTotal += float(thisSale)

if oldItem != None:
    print oldItem, "\t", itemTotal
