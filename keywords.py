import boto3
import json
import csv
import pandas as pd
import sys


#initalize AWS comprehend
comprehend = boto3.client(service_name ='comprehend', region_name = 'us-east-1')
res = []
ASRS_rows = []

#create DF of ASRS DB
with open('ASRS_DBOnline.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rows = list(reader)
    features = rows[0]
    rows = rows[2:]

    for row in rows:
    	ASRS_rows.append(row)

     

    csvfile.close()


ASRS_cols = []
for feature in features:
    ASRS_cols.append(feature)


ASRS_DF = pd.DataFrame(ASRS_rows, columns=ASRS_cols)
ASRS_DF.columns = [c.replace(' ', '_') for c in ASRS_DF.columns]




reportSynopsis = []
check = 0

for r in (ASRS_DF['Report_Synopsis']):
	check +=1
	
	if r == '' or sys.getsizeof(r) > 4999:
		reportSynopsis.append('')
	else:
		reportSynopsis.append(comprehend.detect_key_phrases(Text=r,LanguageCode='en')['KeyPhrases'])

	
	
	





name  = 'synopsiskeywords.txt'
file = open(name,'w')





for e in zip(reportSynopsis):
	#file.write('Report One Narrative ' + json.dumps(a) + 'Report One Callback ' + json.dumps(b) + 'Report Two Narrative ' + json.dumps(c) + 'Report Two Callback ' + json.dumps(d) +  'Report Synopsis ' + json.dumps(e))
	file.write('Report Synopsis ' + json.dumps(e))

	file.write('\n')


file.close()









