#!/usr/bin/python

import sys
from bs4 import BeautifulSoup 
import urllib.request
import json
import xlsxwriter

newlist = []
excellist1 = []
excellist2 = []
filename1 = r"C:\Users\Ryan\Documents\WebScience\Assignment2\output.txt"
value = 0
with open(filename1, "r") as file:
	for line in file:
		url = "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/" + line
		value = value +1
		try:
			response = urllib.request.urlopen(url)
			soup = BeautifulSoup(response, 'html.parser')
			
			filename = r"C:\Users\Ryan\Documents\WebScience\Assignment2\output1.txt"
			outfile = open(filename, 'w')
			outfile.write(str(soup))
			outfile.close()
			
			print("Here:" , value)
			count = 0
			with open(filename, "r") as file:
				for line1 in file:
					if line1.find('memento'):
						count = count + 1
			print("Count is:", count)
			newlist.append(line + " " +str(count))
			excellist1.append(line)
			excellist2.append(count)
		except:
			print(value)
			newlist.append(line+ ' 0')
			excellist1.append(line)
			excellist2.append(0)
			pass
print("List Done")
#print(newlist)
filename = r"C:\Users\Ryan\Documents\WebScience\Assignment2\output2.txt"
outfile = open(filename, 'w')
outfile.write("\n".join(newlist))
outfile.close()

#excel Worksheet
filename2 = r'C:\Users\Ryan\Documents\WebScience\Assignment2\Histogram1.xlsx'
workbook = xlsxwriter.Workbook(filename2)
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold' : 1})

#data headers
worksheet.write('A1', 'URI', bold)
worksheet.write('B1', 'Num of Mementos', bold)

row = 1
col = 0

#throw data into 
for URI in excellist1:
	worksheet.write_string(row, col, URI)
	row += 1

row1 = 1
col1 = 1	
for Number in excellist2:
	worksheet.write_number(row1, col1, Number)
	row1 += 1
	
workbook.close()
