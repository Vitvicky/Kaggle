#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import pylab
import numpy as np

import seaborn as sns
sns.set(style="white", color_codes=True)
filePath = 'F:/UTD/Match/Crime/train.csv'
trainData = pd.read_csv(filePath)
#print trainData.head()
plt.figure();

#trainData.groupby('Category').size().plot(kind='bar')
#plt.show()
weekData = trainData[trainData['Category']=='LARCENY/THEFT']
sns.countplot(x='DayOfWeek', data=weekData)

Resolution = trainData.groupby('Resolution').size().plot(kind='bar')
#plt.show()

PdDistrict = trainData.groupby('PdDistrict').size().plot(kind='bar')
plt.show()

timeData = pd.read_csv(filePath, parse_dates=['Dates'], index_col='Dates')
timeData['Hour'] = timeData.index.hour
timeData['Month'] = timeData.index.month
timeData['Day'] = timeData.index.day

#analysis of hour
pylab.rcParams['figure.figsize'] = (14.0, 8.0)
with plt.style.context('fivethirtyeight'):
    ax1 = plt.subplot2grid((1,1), (0,0), colspan=3)
    ax1.plot(timeData.groupby('Hour').size(), 'ro-')
    ax1.set_title ('All crimes Occurence by Hour')
    start, end = ax1.get_xlim()
    ax1.xaxis.set_ticks(np.arange(start, end, 1))
    
    pylab.gcf().text(0.5, 1.03, 
                    'Crime Occurence by Hour',
                     horizontalalignment='center',
                     
                     fontsize = 28)
#plt.show()

#analysis of month
pylab.rcParams['figure.figsize'] = (16.0, 8.0)
monthsIdx = timeData.groupby('Month').size().keys() - 1
monthsLabel = ['January', 'February', 
             'March', 'April', 'May', 
             'June', 'July','August', 
             'September', 'October', 'Novemeber', 'December']
occursByMonth = timeData.groupby('Month').size().get_values()
ax1 = plt.subplot2grid((1,1), (0,0), colspan=3)
ax1.plot(monthsIdx, occursByMonth, 'ro-', linewidth=2)

ax1.set_title ('All Crimes Occurence by Month', fontsize=20)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
#plt.show()