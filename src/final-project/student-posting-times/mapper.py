#!/usr/bin/python
"""
Students and Posting Time on Forums

We have a lot of passionate students that bring a lot of value to forums.
Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them,
that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators.
These are usually chosen from students who already have shown that they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what times of day the activity is the highest,
and to know which of the students are active at that time.

In this exercise your task is to find for each student what is the hour during which the student has posted the most posts.
Output from reducers should be:

author_id    hour

For example:

13431511\t13
54525254141\t21
If there is a tie: there are multiple hours during which a student has posted a maximum number of posts,
please print the student-hour pairs on separate lines. You can ignore the time-zone offset for all times - for example in the following
line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.
"""

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        try:
            if(len(line)) == 19:
                id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
                hour = re.findall(r'.*? (\d{2}):.*?', added_at)[0]
                print "{0}\t{1}".format(author_id, hour)
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    mapper()
