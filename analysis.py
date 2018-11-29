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



reportOneNarrative = []
reportOneCallback = []
reportTwoNarrative = []
reportTwoCallback = []
reportSynopsis = []
check = 0

for a in (ASRS_DF['Report_1_Narrative']):
	check +=1
	if check > 50:
		break
	if a == '' or sys.getsizeof(a) > 4999:
		reportOneNarrative.append('')
	else:
		reportOneNarrative.append(comprehend.detect_key_phrases(Text=a,LanguageCode='en')['KeyPhrases'])
check = 0
for b in (ASRS_DF['Report_1_Narrative']):
	check +=1
	if check > 50:
		break
	if b == '' or sys.getsizeof(b) > 4999:
		reportOneCallback.append('')
	else:
		reportOneCallback.append(comprehend.detect_key_phrases(Text=b,LanguageCode='en')['KeyPhrases'])
check = 0 
for c in (ASRS_DF['Report_2_Narrative']):
	check +=1
	if check > 50:
		break
	if c == '' or sys.getsizeof(c) > 4999:
		reportTwoNarrative.append('')
	else:
		reportTwoNarrative.append(comprehend.detect_key_phrases(Text=c,LanguageCode='en')['KeyPhrases'])
check = 0
for d in (ASRS_DF['Report_2_Callback']):
	check +=1
	if check > 50:
		break
	if d == '' or sys.getsizeof(d) > 4999:
		reportTwoCallback.append('')
	else:
		reportTwoCallback.append(comprehend.detect_key_phrases(Text=d,LanguageCode='en')['KeyPhrases'])
check = 0
for e in (ASRS_DF['Report_Synopsis']):
	check +=1
	if check > 50:
		break
	if e == '' or sys.getsizeof(e) > 4999:
		reportSynopsis.append('')
	else:
		reportSynopsis.append(comprehend.detect_key_phrases(Text=e,LanguageCode='en')['KeyPhrases'])

	
	
	





name  = 'keywords.txt'
file = open(name,'w')





for a,b,c,d,e in zip(reportOneNarrative,reportOneCallback,reportTwoNarrative,reportTwoCallback,reportSynopsis):
	file.write('Report One Narrative ' + json.dumps(a) + 'Report One Callback ' + json.dumps(b) + 'Report Two Narrative ' + json.dumps(c) + 'Report Two Callback ' + json.dumps(d) +  'Report Synopsis ' + json.dumps(e))
	file.write('\n')


file.close()









