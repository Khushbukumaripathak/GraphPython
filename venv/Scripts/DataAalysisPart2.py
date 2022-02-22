import matplotlib.pyplot as plt
import csv
import datetime
from datetime import timezone

x = []
y = []

with open('.\\cc220GatewayLog-2021-06-02.log\\24EDFD000053-AA90-2021-06-02.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		date_time = datetime.datetime.strptime(row[0],"%m/%d/%Y %I:%M:%S%p")
		if len(x) != 0:
			previous_date = datetime.datetime.strptime(x[len(x) - 1],"%m/%d/%Y %I:%M:%S%p")
			previous_date = previous_date + datetime.timedelta(hours=1)
		if len(x)==0:
			x.append(row[0])
		elif previous_date == date_time:
			x.append(row[0])
		y.append(row[1])

#plt.plot(x, y, color = 'g', linestyle = 'dashed',
		#marker = 'o',label = "Signal Data")

plt.plot([2,4], [1,2,3,4])

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Signal')
plt.title('Signal Report', fontsize = 10)
plt.grid()
plt.legend()
plt.show()
