#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    prevUser = None
    currentUser = None

    id = title = tagnames = author_id = node_type = parent_id = abs_parent_id = added_at = score = reputation = gold = silver = bronze = ""
    source = None

    for line in reader:
        if(len(line) == 10):
            currentUser, source, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = line
        else:
            currentUser, source, reputation, gold, silver, bronze = line

        if prevUser and prevUser != currentUser:
            writer.writerow([id, title, tagnames, prevUser, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, bronze])

        prevUser = currentUser

    if prevUser != None:
        writer.writerow([id, title, tagnames, prevUser, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, bronze])

if __name__ == "__main__":
    reducer()
