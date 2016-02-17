import subprocess
from bs4 import BeautifulSoup 
import urllib.request
import base64
import hashlib
import xml.etree
import re

filename1 = r"C:\Users\Ryan\Documents\WebScience\Assignment3\output.txt"
value = 0
urls=[]

def outputfile(link, value, count):

	try:
		response = urllib.request.urlopen(link)
		soup = BeautifulSoup(response, 'html.parser')
					
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment3\Raw_html_Files\\"+str(value)+".txt"
		outfile = open(filename, 'w')
		outfile.write(str(soup.encode('utf8')))
		outfile.close()
	except:
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment3\Raw_html_Files\\"+str(value)+".txt"
		outfile = open(filename, 'w')
		outfile.write("No HTML")
		outfile.close()
		print("Here")
		pass
		
	count += 1
	return count
	
def removetags():

	temp = 1
	while temp < 1001:
		stringers = ''
		print("Iterator:", temp)
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment3\Raw_html_Files\\"+str(temp)+".txt"
		text = open(filename, 'r')
		for line in text:
			stringers += line
		
		cleanr =re.compile('<.*?>')
		cleantext = re.sub(cleanr,'', stringers)
		
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment3\Processed_html_Files\\"+str(temp)+".txt"
		outfile = open(filename, 'w')
		outfile.write(str(cleantext))
		outfile.close()
		temp += 1
			
def begin():	
	with open(filename1, "r") as file:
		count = 0
		temp = 0
		for line in file:
			value = value + 1
			url = line
			count = outputfile(url, value, count)
			temp = temp+1
			print("Index",temp)
			
begin()
removetags()
print("Done")