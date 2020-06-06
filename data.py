import numpy as np
import pandas as pd
import random 
import math 
import time
from sklearn.model_selection import RandomizedSearchCV,train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error,mean_absolute_error
import datetime 
import operator


confirmed_cases=pd.read_csv('E:\covid-19 outbreak prediction\confirmed.csv')






deaths_reported=pd.read_csv('E:\covid-19 outbreak prediction\deaths.csv')





recovered_cases=pd.read_csv(r'E:\\covid-19 outbreak prediction\\recovered.csv')



cols=confirmed_cases.keys()










confirmed= confirmed_cases.loc[:, cols[4]:cols[-1]]
deaths=deaths_reported.loc[:, cols[4]:cols[-1]]
recoveries = recovered_cases.loc[:, cols[4]:cols[-1]]








dates= confirmed.keys()
world_cases = []
total_deaths = []
mortality_rate = []
total_recovered = []

for i in dates:
    confirmed_sum = confirmed[i].sum()
    death_sum = deaths[i].sum()
    recovered_sum = recoveries[i].sum()
    world_cases.append(confirmed_sum)
    total_deaths.append(death_sum)
    mortality_rate.append(death_sum/confirmed_sum)
    total_recovered.append(recovered_sum)
    
    















days_since_1_22 = np.array([i for i in range(len(dates))]).reshape(-1,1)
world_cases = np.array(world_cases).reshape(-1,1)
total_deaths = np.array(total_deaths).reshape(-1,1)
total_recovered = np.array(total_recovered).reshape(-1,1)









days_in_future = 10
future_forecast = np.array([i for i in range(len(dates)+days_in_future)]).reshape(-1,1)
adjusted_dates = future_forecast[:-10]










start = '1/22/2020'
start_date = datetime.datetime.strptime(start,"%m/%d/%Y")
future_forecast_dates= []
for i in range(len(future_forecast)):
    future_forecast_dates.append((start_date+datetime.timedelta(days=i)).strftime('%m/%d/%Y'))





latest_cnf = confirmed_cases[dates[-1]]
latest_deaths = deaths_reported[dates[-1]]
latest_recover = recovered_cases[dates[-1]]







unq_countries = list(confirmed_cases['Country/Region'].unique())









county_cnf_cases = []
no_cases =[]
for i in unq_countries:
    cases = latest_cnf[confirmed_cases['Country/Region']==i].sum()
    if cases > 0:
        county_cnf_cases.append(cases)
    else:
        no_cases.append(i)
        
for i in no_cases:
    unq_countries.remove(i)
    
unq_countries = [k for k,v in sorted(zip(unq_countries,county_cnf_cases),key=operator.itemgetter(1),reverse=True)]
    
for i in range(len(unq_countries)):
    county_cnf_cases[i] = latest_cnf[confirmed_cases['Country/Region']==unq_countries[i]].sum()





print('confirmed cases country wise:')
for i in range(len(unq_countries)):
    print(f'{unq_countries[i]} : {county_cnf_cases[i]}  ')





unq_provinces = list(confirmed_cases['Province/State'].unique())
#  outliers = ['United Kingdom','Denmark','France']
#  for i outliers:
#      unq_provinces.remove(i)





province_cnf_cases = []
no_cases =[]
for i in unq_provinces:
    cases = latest_cnf[confirmed_cases['Province/State']==i].sum()
    if cases > 0:
     
        province_cnf_cases.append(cases)
    else:
        no_cases.append(i)

        
for i in no_cases:
    unq_provinces.remove(i)





for i in range(len(unq_provinces)):
    print(f'{unq_provinces[i]} : {province_cnf_cases[i]}')





nan = []
for i in range(len(unq_provinces)):
    if type(unq_provinces[i])==float:
        nan.append(i)
unq_provinces=list(unq_provinces)
province_cnf_cases=list(province_cnf_cases)

for i in nan:
    unq_provinces.pop(i)
    province_cnf_cases(i)








vis_countries=[]
vis_cases =[]
others = np.sum(county_cnf_cases [10:])
for i in range(len(county_cnf_cases[:10])):
    vis_countries.append(unq_countries[i])
    vis_cases.append(county_cnf_cases[i])
    










vis_countries.append('Others')
vis_cases.append(others)














