import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
from dateutil.rrule import rrule, DAILY
import itertools
from tkinter import *
from tkinter import filedialog

y = []
time = []
#file_name = '.\\dist\\Gateway\\Messages\\24EDFD0000C4-AA90-2021-07-23.csv'
print('Select file path: ')
#file_name = str(input())
input = filedialog.askopenfile(initialdir="/")
file_name = input.name

with open(file_name,'r') as csvfile:
	lines = list(csv.reader(csvfile, delimiter=';'))

for row in lines:
    time.append(row[0])
    if (file_name.__contains__('B080') | file_name.__contains__('B081') | file_name.__contains__('B082')):
        #print(row[2:-1])
        values = row[2:-1]
        g_values = [int(value) / 32767 * 16 for value in values]
        x_p2p = max(g_values) - min(g_values)
        y.append(x_p2p)
    else:
        y.append(float(row[1]))

fig, ax = plt.subplots()

#ax.scatter(time, y)
if(file_name.__contains__('AA90')):
    ax.plot(time, y, color='firebrick', alpha=0.3, marker='o')

elif(file_name.__contains__('RSSI')):
    ax.plot(time, y, color='green', alpha=0.3, marker='o')

elif (file_name.__contains__('B080')):
    ax.plot(time, y, color='red', alpha=0.3, marker='o')

elif(file_name.__contains__('B081')):
    ax.plot(time, y, color='blue', alpha=0.3, marker='o')

elif (file_name.__contains__('B082')):
    ax.plot(time, y, color='skyblue', alpha=0.3, marker='o')

sensor_name = file_name.split('\\')[-1]
ax.set(title= sensor_name+' Report', ylabel='Data', xlabel='Dates')

rule = rrulewrapper(DAILY, dtstart=dt.datetime.strptime(lines[0][0],"%m/%d/%Y %I:%M:%S %p"), interval=33)
loc = RRuleLocator(rule)
ax.xaxis.set_major_locator(loc)
ax.grid()
ax.set_xlim(time[0], time[-1])
#ax.set_ylim(y[-1], y[0])
ax.set_ylim(min(y)-1, max(y)+1)
ax = plt.gca()
plt.gcf().autofmt_xdate()
plt.show()
