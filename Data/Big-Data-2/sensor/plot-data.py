#!/usr/bin/python

import sys
import re
import time
from matplotlib import pyplot
import matplotlib.dates as mdate
from pytz import timezone

x = []
y = []

file = open(sys.argv[1], 'r')
for line in file:
    parts = re.split("\s+", line)
    
    data = parts[1].split(",")

    for field in data:
        match = re.match(sys.argv[2] + '=(\d+\.\d+).*', field)
        if match:
            timestamp = float(parts[0])
            x.append(timestamp)
            #time_parts = time.localtime(timestamp)
            y.append(float(match.group(1)))
    
file.close()

#fig, ax = pyplot.subplots()
fig = pyplot.figure()
ax = fig.add_subplot(111)

secs = mdate.epoch2num(x)

ax.plot_date(secs, y)

pyplot.xlabel('time')
pyplot.ylabel(sys.argv[2])

date_formatter = mdate.DateFormatter('%H:%M.%S', tz=timezone('US/Pacific'))
ax.xaxis.set_major_formatter(date_formatter)
fig.autofmt_xdate()

pyplot.show()
