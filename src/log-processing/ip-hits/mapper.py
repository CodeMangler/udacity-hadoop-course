#!/usr/bin/python

# 10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/css/960.css HTTP/1.1" 304 -

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, datetime, tz, method, page, http_version, status, content_size = data
        print "{0}\t{1}".format(ip, 1)
