import os.path
import csv
import pandas as pd
from pandas import Series, DataFrame

files = ['AIDS_REPORTS_MA.csv', 'AIDS_REPORTS_ME.csv', 'AIDS_REPORTS_NH.csv', 'AIDS_REPORTS_VT.csv']
all_states = []

for f in files:
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
        features = rows[0]
        rows = rows[1:]

        for row in rows:
            all_states.append(row)

        csvfile.close()


faa_cols = []
for feature in features:
    faa_cols.append(feature)

new_england = pd.DataFrame(all_states, columns=faa_cols)
new_england = new_england.drop(['Aircraft Damage', 'Engine Group Code', 'Nbr of Engines'], axis=1)


#Filter data for fatal Aircraft incidents
fatal = []
for row in new_england.itertuples(index=False):
    if int(row[16]) > 0:
        fatal.append(row)

fatal = pd.DataFrame(fatal, columns=new_england.columns)

#now do non_fatal
non_fatal = []
for row in new_england.itertuples(index=False):
    if int(row[16]) == 0:
        non_fatal.append(row)

non_fatal = pd.DataFrame(non_fatal, columns=new_england.columns)
