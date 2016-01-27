#!/usr/bin/python

import sys
from bs4 import BeautifulSoup 
import urllib.request

#Links I Used
#url = "http://onlinelibrary.wiley.com/doi/10.1002/cpe.710/abstract"
#url = "http://www.cs.odu.edu/~mln/teaching/cs532-s16/test/pdfs.html"
#url = "https://helpx.adobe.com/acrobat/kb/link-html-pdf-page-acrobat.html"

url = sys.argv[1]
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response)
count = 0
print("Files Extracted:")
for links in soup.find_all('a'):
	try:
		response1 = urllib.request.urlopen(links.get('href'))
		print(links.get('href'))
		count = count + 1
	except:
		pass
print("Number of Pages is: " + str(count))
print(" ")
pdfcount = 0
print("PDF Files are: ")
for links in soup.find_all('a'):
	try:
		response1 = urllib.request.urlopen(links.get('href'))
		if response1.info()['Content-type'] == "application/pdf":
			print(links.get('href'))
			print("Content-type: ", response1.info()['Content-type'])
			print("The byte size is: ", response1.info()['Content-Length'])
			print(" ")
			pdfcount = pdfcount +1
	except:
		pass
print("Number of PDFs is: " + str(pdfcount))
print("The response code:", response.code)