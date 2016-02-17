import re
import xlsxwriter

list = ['1','2','11','12','13','17','21','22','24','29']
storenumber = []
uri = []
def QuerySearch(word):

	temp = 1
	while temp < 1001:
		print("Iterator:", temp)
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment3\Processed_html_Files\\"+str(temp)+".txt"
		with open(filename, 'r') as text:
			for line in text:
				if word in line:
					print("Found", str(temp))
					storenumber.append(str(temp))
		temp += 1

def DetermineTF(word):
	for temp in list:
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment3\Processed_html_Files\\"+str(temp)+".txt"
		text = open(filename, 'r')
		contents = text.read()
		text.close()
		words = re.split("\W+",contents.lower())
		words_count = len(words)
		print("Number of '" + word + "' in file", contents.count(word))
		print("Number of Total Words in file", words_count)

QuerySearch('game')
print(storenumber)
print(len(storenumber))	
	
DetermineTF('game')
