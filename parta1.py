#!/usr/bin/env python
# coding: utf-8

# In[7]:



import os
os.getcwd()


# In[39]:

import sys
import pandas as pd
covid = pd.read_csv('owid-covid-data.csv')

covid=covid[['date','location','total_cases','new_cases','total_deaths','new_deaths']]
from datetime import datetime as dt
i=0
year=[]
year=[0 for i in range(len(covid.date))]
month=[]
month=[0 for i in range(len(covid.date))]

for date in covid.date:
   year[i]=int('{:%Y}'.format(dt.strptime(date, '%Y/%m/%d')) )
   month[i]=int('{:%m}'.format(dt.strptime(date, '%Y/%m/%d')) )
   i=i+1
covid['year']=year
covid['month']=month

covid_2020=covid[covid.year==2020]
grouped=covid_2020.groupby(['location','month'],sort=False)
i=0
total_cases=[]
total_cases=[0 for i in range(len(grouped))]
total_deaths=[]
total_deaths=[0 for i in range(len(grouped))]
i=0
i=0
for k,gp in grouped:
    total_cases[i]=gp.total_cases.iloc[-1]


    total_deaths[i]=gp.total_deaths.iloc[-1]
    i+=1
  

agg_group=grouped.sum(min_count=1)
agg_group=agg_group.reset_index()
del agg_group['year']
agg_group['total_cases']=total_cases
agg_group['total_deaths']=total_deaths
print(agg_group.loc[:4,:])
covid = pd.read_csv('owid-covid-data.csv')
case_fatality_rate=agg_group.new_deaths/agg_group.new_cases
agg_group['case_fatality_rate']=case_fatality_rate
task1=agg_group[['location','month','case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths']]
print(task1.loc[:4,:])
task1.to_csv(sys.argv[1])

