#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    prevThread = None
    currentThread = None
    authors = []

    for line in reader:
        if(len(line) == 2):
            currentThread, author = line

        if prevThread and prevThread != currentThread:
            writer.writerow([prevThread, ','.join(authors)])
            authors = []

        prevThread = currentThread
        authors.append(author)

    if prevThread != None:
        writer.writerow([prevThread, ','.join(authors)])

if __name__ == "__main__":
    reducer()
