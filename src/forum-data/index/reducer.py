#!/usr/bin/python

import sys

def reducer():
    prevWord = None
    nodes = []

    for line in sys.stdin:
        data_mapped = line.strip().split(' ')
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        currentWord, node_id = data_mapped

        if prevWord and prevWord != currentWord:
            print prevWord, "\t", sorted(nodes), "\t", len(nodes)
            prevWord = currentWord;
            nodes = []

        prevWord = currentWord
        nodes.append(int(node_id))

    if prevWord != None:
        print prevWord, "\t", sorted(nodes), "\t", len(nodes)

if __name__ == "__main__":
    reducer()
