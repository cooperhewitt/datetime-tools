#!/usr/bin/env python

import sys
import dateutil.parser

t = " ".join(sys.argv[1:])
t = dateutil.parser.parse(t)

"""
    http://codeghar.wordpress.com/2007/12/06/manage-time-in-ubuntu-through-command-line/
    ...where newdatetimestring has to follow the format nnddhhmmyyyy.ss which is described below

    nn is a two digit month, between 01 to 12
    dd is a two digit day, between 01 and 31, with the regular rules for days according to month and year applying
    hh is two digit hour, using the 24-hour period so it is between 00 and 23
    mm is two digit minute, between 00 and 59
    yyyy is the year; it can be two digit or four digit: your choice. I prefer to use four digit years whenever I can for better clarity and less confusion
    ss is two digit seconds. Notice the period . before the ss.
"""

d = t.strftime('%m%d%H%M%Y.%S')
print d
