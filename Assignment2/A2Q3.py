import json
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re
import urllib.request
from bs4 import BeautifulSoup 
import os
import xlsxwriter


#index = 0

#number of mementos with 0 urls
#count = 0

#lists of mementos and urls
mementos = []
urls = []
createdate = []
date = []

def CurlForReponse(num):

	print("Number of urls with 0 momentos:", num)
	index = 0
	dation = 0
	for line in urls:
		filename = r"http://cd.cs.odu.edu/cd?url=" + line
		print(index+1)
		try:
			response = urllib.request.urlopen(filename)
			soup = BeautifulSoup(response, 'html.parser')

			#print(str(soup))

			filename = r"C:\Users\Ryan\Documents\WebScience\Assignment2\CarbonDate.txt"
			outfile = open(filename, 'w')
			outfile.write("".join(str(soup)))
			outfile.close()
				
			dation += GetCreationDate(index)
			index = index + 1	
			#print(dation)
		except:
			#createdate.append(urls[index] + " 0")
			date.append(" 0")
			index = index + 1
		
	outputExcel(urls, date, mementos, num, dation)
	

def GetCreationDate(num):

	filename1 = r"C:\Users\Ryan\Documents\WebScience\Assignment2\CarbonDate.txt"
	value = 0
	numofnocreationdation = 0
	with open(filename1, "r") as file:
		for line in file:
			value +=1
			if value == 4:
				#print("Line length:", len(line))
				#print(urls[num])
				if line[30:len(line)-3] == "":
					numofnocreationdation = numofnocreationdation + 1
					#createdate.append(urls[num] + " 0")
					date.append(" 0")
				else:
					#createdate.append(urls[num] + line[30:len(line)-3])
					date.append(str(line[30:len(line)-12]))
					print(line[30:len(line)-12])
	
	return numofnocreationdation
	
	
				
def storeMementosandURls():

	filename3 = r"C:\Users\Ryan\Documents\WebScience\Assignment2\output2.txt"
	val = 0
	with open(filename3, "r") as file:
		for line in file:
			if val == 0:
				urls.append(line)
				#print(line)
				val = val + 1
			elif val == 1:
				mementos.append(int(line))
				#print(line)
				val = 0
	count = 0
	for moment in mementos:
		if moment == 0:
			count = count + 1
			
	CurlForReponse(count)
			
def outputExcel(link, dated, mems, numcount, numcreate):

	#for temp1 in dated:
	#	print(temp1)
			
	#excel Worksheet
	filename2 = r'C:\Users\Ryan\Documents\WebScience\Assignment2\Graph.xlsx'
	workbook = xlsxwriter.Workbook(filename2)
	worksheet = workbook.add_worksheet()

	bold = workbook.add_format({'bold' : 1})

	#data headers
	worksheet.write('A1', 'URI', bold)
	worksheet.write('B1', 'Creation Dates', bold)
	worksheet.write('C1', 'Num of Mementos', bold)
	worksheet.write('D1', 'Mementos with 0', bold)
	worksheet.write('E1', 'URIs with no dates', bold)

	row = 1
	col = 0

	#throw data into 
	for URI in link:
		worksheet.write_string(row, col, URI)
		row += 1

	row1 = 1
	col1 = 1	
	for months in dated:
		worksheet.write_string(row1, col1, months)
		row1 += 1

	row2 = 1
	col2 = 2
	for memo in mems:
		worksheet.write_number(row2, col2, memo)
		row2 += 1	
	
	worksheet.write_number(2, 4, numcount)
	worksheet.write_number(2, 5, numcreate)
	
	workbook.close()
	
	print("Done")
		
storeMementosandURls()
