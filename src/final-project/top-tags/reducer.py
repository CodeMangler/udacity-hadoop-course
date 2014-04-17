#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    prevTag = None
    currentTag = None
    question_id = None
    tags = {}
    tag_counts = {}

    for line in reader:
        if(len(line) == 2):
            currentTag, question_id = line

            if(not tags.has_key(currentTag)):
                tags[currentTag] = []
                tag_counts[currentTag] = 0

            tags[currentTag].append(question_id)
            tag_counts[currentTag] = tag_counts[currentTag] + 1

    top_ten_tag_counts = sorted(tag_counts.values())[0:10]
    top_ten_tags = map(lambda count_tuple: count_tuple[0], sorted(tag_counts.items(), reverse=True, key=lambda count_tuple: count_tuple[1])[:10])

    for tag in top_ten_tags:
        writer.writerow([tag, ','.join(tags[tag])])

if __name__ == "__main__":
    reducer()
