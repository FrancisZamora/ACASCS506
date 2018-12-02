
import boto3
import json 
import sys
import csv
import pandas as pd
#initialize AWS comprehend 
comprehend = boto3.client(service_name ='comprehend', region_name = 'us-east-1')
ASRS_rows = []
ASRS_cols = []
#create DF of ASRS DB
with open('ASRS_DBOnline.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rows = list(reader)
    features = rows[0]
    rows = rows[2:]

    for row in rows:
    	ASRS_rows.append(row)

     

    csvfile.close()


for feature in features:
    ASRS_cols.append(feature)


ASRS_DF = pd.DataFrame(ASRS_rows, columns=ASRS_cols)
ASRS_DF.columns = [c.replace(' ', '_') for c in ASRS_DF.columns]






reportSynopsis = []


for r in (ASRS_DF['Report_Synopsis']):
	print(r)
	if r == '' or sys.getsizeof(r) > 4999:
		reportSynopsis.append('')
	else:
		reportSynopsis.append(comprehend.detect_entities(Text=r,LanguageCode='en')['Entities'])




name  = 'synopsisentities.txt'
file = open(name,'w')





for r in (reportSynopsis):
	file.write('Report Synopsis Entities ' + json.dumps(r))
	file.write('\n')


file.close()
