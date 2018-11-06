import boto3
import json
import csv
import pandas as pd

#initalize AWS comprehend
comprehend = boto3.client(service_name ='comprehend', region_name = 'us-east-1')
res = []
ASRS_rows = []

#create DF of ASRS DB
with open('ASRS_DBOnline.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rows = list(reader)
    features = rows[0]
    rows = rows[1:]

    for row in rows:
    	ASRS_rows.append(row)

     

    csvfile.close()


ASRS_cols = []
for feature in features:
    ASRS_cols.append(feature)


ASRS_DF = pd.DataFrame(ASRS_rows, columns=ASRS_cols)


# get reports 
clean_synopsis = []
'''
for i in ASRS_DF.iterrows():
	clean_synopsis.append(i['Report 1'])

print(clean_synopsis)    	
'''


#convert to list        
for i in ASRS_DF['Report 1']:
	print(i)

text = "The weather in boston is pretty trash"

print("Detecting Key Phrases")
print(json.dumps(comprehend.detect_key_phrases(Text=text,LanguageCode='en'),sort_keys = True,indent=4))




