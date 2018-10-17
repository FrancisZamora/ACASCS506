from collections import defaultdict
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import ssl
#for https
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)


#dictionary to count the frequency of words in a given document
table = defaultdict(int)
#link for page to parse
faa = "https://www.asias.faa.gov/apex/f?p=100:11:::NO:::"

#get html from link
faaHtml =  urlopen(faa, context = gcontext).read()

#create soup of html
faaSoup = BeautifulSoup(faaHtml,'html.parser')

#get text from soup, not completely clean for FAA but it works
faaText = faaSoup.get_text()

#create list of individual words
faaList = faaText.split(' ')

#go through list and get frequency
for i in faaList:
	if table[i] in table.keys():
		table[i] +=1
	else:
		table[i]  = 1 
print(table)





