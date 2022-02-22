#import pandas as pd

#df=pd.read_excel(r'24EDFD0000EC-RSSI-2021-07-07.csv')
#print(df)

import matplotlib.pyplot as plt
import csv

Data = []
Date = []

with open('24EDFD0000EC-RSSI-2021-07-07.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		Data.append(row[0])
		Date.append(row[1])

plt.scatter(Date, Data, color = 'g',s = 10)
plt.xticks(rotation = 10)
plt.xlabel('Data')
plt.ylabel('Date')
plt.title('Data graph', fontsize = 10)

plt.show()
