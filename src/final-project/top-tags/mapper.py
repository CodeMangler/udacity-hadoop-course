#!/usr/bin/python
"""
Top Tags

We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

For an extra challenge you can think how to get a top 10 list of tags, where they are ordered by some weighted score by your choice.
"""

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if(len(line)) == 19:
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
            if(node_type == 'question'):
                tags = tagnames.lower().split(' ')
                for tag in tags:
                    writer.writerow([tag, id])

if __name__ == "__main__":
    mapper()
