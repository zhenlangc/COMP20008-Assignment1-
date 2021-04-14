#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Part A Task2
import pandas as pd
import sys
covid = pd.read_csv('owid-covid-data.csv')
covid=covid[['date','location','total_cases','new_cases','total_deaths','new_deaths']]
from datetime import datetime as dt
i=0
year=[]
year=[0 for i in range(len(covid.date))]


for date in covid.date:
   year[i]=int('{:%Y}'.format(dt.strptime(date, '%Y/%m/%d')) )
   
   i=i+1
covid['year']=year


covid_2020=covid[covid.year==2020]
gp_year=covid_2020.groupby(['location'],sort=False)


agg_gp=gp_year.sum(min_count=1)
agg_gp=agg_gp.reset_index()
del agg_gp['year']
agg_gp
case_fatality_rate=agg_gp.new_deaths/agg_gp.new_cases
agg_gp['case_fatality_rate']=case_fatality_rate
task1=agg_gp[['location','case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths']]

import pandas as pd
import matplotlib.pyplot as plt
plt.subplot(2, 1, 1)
plt.scatter(agg_gp.new_cases,case_fatality_rate,color='red')
plt.grid(True)
plt.savefig(sys.argv[1])
plt.title('case_fatality_rate vs new_cases')
plt.xlabel('new_cases')
plt.ylabel('case_fatality_rate')

plt.subplot(2, 1, 2)
ag_n=agg_gp[agg_gp.new_cases>0]
plt.scatter(ag_n.new_cases,ag_n.case_fatality_rate,color='red')
plt.grid(True)
plt.xscale('log')
plt.savefig(sys.argv[2])
plt.title('case_fatality_rate vs new_cases with semilog')
plt.xlabel('new_cases with log transform')
plt.ylabel('case_fatality_rate')

