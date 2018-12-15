import os.path
import csv
import pandas as pd
from pandas import Series, DataFrame
from FAA_filter import *


#print(new_england.columns)

"""
drop
state
airport
event type
ac damage
flight phase
ac series
operator
engine make
engine model
engine group code
registration number
"""

new_england = new_england.drop(['Local Event Date', 'Event State', 'Event Airport', 'Event Type',
        'Flight Phase', 'Aircraft Series', 'Operator', 'Aircraft Registration Nbr',
        'Aircraft Engine Make', 'Aircraft Engine Model', ' '], axis=1)

#preprocessing and changing missing vals
hrs = new_england['PIC Flight Time Total Hrs'].replace('', 0)
hrs = hrs.astype(int)

agg_hrs = 0
for val in hrs:
    agg_hrs += val

avg_hrs = agg_hrs/ hrs.size
hrs = hrs.replace(0, avg_hrs)
new_england['PIC Flight Time Total Hrs'] = hrs
#print(new_england['PIC Flight Time Total Hrs'])


#same process different data
model_hrs = new_england['PIC Flight Time Total Make-Model'].replace('', 0)
model_hrs = model_hrs.astype(int)
agg_model_hrs = 0
for val in model_hrs:
    agg_model_hrs += val

avg_model_hrs = agg_model_hrs/ model_hrs.size
model_hrs = model_hrs.replace(0, avg_model_hrs)
new_england['PIC Flight Time Total Make-Model'] = model_hrs
#print(new_england['PIC Flight Time Total Make-Model'])


df_city = pd.get_dummies(new_england['Event City'], prefix = 'city')
df_aMake = pd.get_dummies(new_england['Aircraft Make'], prefix = 'aMake')
df_aModel = pd.get_dummies(new_england['Aircraft Model'], prefix = 'aModel')
df_ftype = pd.get_dummies(new_england['Primary Flight Type'], prefix = 'flightType')
df_conduct = pd.get_dummies(new_england['Flight Conduct Code'], prefix = 'cinduct')
df_plancode = pd.get_dummies(new_england['Flight Plan Filed Code'], prefix = 'planCode')
df_cert = pd.get_dummies(new_england['PIC Certificate Type'], prefix = 'cert')


df_final = pd.concat([new_england, df_city, df_aMake, df_aModel, df_ftype, df_conduct,
        df_plancode, df_cert], axis=1)

df_final = df_final.drop( ['Event City', 'Aircraft Make', 'Aircraft Model',
        'Primary Flight Type', 'Flight Conduct Code', 'Flight Plan Filed Code',
        'PIC Certificate Type'], axis = 1 )

df_final.to_csv('classification.csv', encoding='utf-8')
new_england.to_csv('new_england.csv', encoding='utf-8')
