import docclass
import feedparser
import re
from sklearn import svm
from sklearn import cross_validation
import numpy as np

def remove_html_tags(data):
  p = re.compile(r'<.*?>')
  return p.sub('', data)
  
def getwords(html):
  # Remove all the HTML tags
	txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
	words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
	return [word.lower() for word in words if word!='']
	

  
def readfile(feed, fisherclassifier):
	# Get feed entries and loop over them
	title =[]
	guess =[]
	actual=[]
	Yvalue = []
	f=feedparser.parse(feed)
	print(len(f))
	count = 0
	for entry in f['entries']:
		count = count + 1
		print(count)
		print ('-----')
		# Print the contents of the entry
		print ('Title: '+str(entry['title'].encode('utf-8')))
		print()
		fulltext = remove_html_tags(entry['title'])
		title.append(str(fulltext))
		#fulltext = fulltext +" " +remove_html_tags(entry['summary'])
		# Print the best guess at the current category
		if count < 20:
			#print('Guess: '+str(fulltext.encode('utf-8')))		
			value = str(fisherclassifier.classify(fulltext))
			print('Guess: '+ value)
			if value == 'None':
				Yvalue.append(0)
			else:
				Yvalue.append(int(value))
			# Ask the user to specify the correct category and train on that
			temp = raw_input('Enter Category:')
			print("value: ",temp)
			actual.append(int(temp))
			fisherclassifier.train(fulltext,temp)
		else:
			value1 = str(fisherclassifier.classify(fulltext))
			print(value1)
			actual.append(int(temp))
		print()
	
	return actual
	
def readVector(filename):
	#lines=[line for line in file(filename)]
	lines=[]
	for line in open(filename):
		lines.append(line)
	
	# First line is the column titles
	colnames=lines[0].strip().split('\t')[1:]
	rownames=[]
	data=[]
	for line in lines[1:]:
		p=line.strip().split('\t')
		# First column in each row is the rowname
		rownames.append(p[0])
		# The data for this row is the remainder of the row
		data.append([float(x) for x in p[1:]])
	return rownames,colnames,data

c2=docclass.fisherclassifier(docclass.getwords)
blognames,words,data=readVector(r'C:\Users\Ryan\Documents\WebScience\Assignment10\blogdata3.txt')
Yvalue = readfile("http://theworldsfirstinternetbaby.blogspot.com/feeds/posts/default?max-results=100&alt=rss", c2)

X_digits = np.array(data)
Y_digits = np.array(Yvalue)

clf = svm.SVC(kernel='linear', C=10)
clf.fit(X_digits, Y_digits)
scores = cross_validation.cross_val_score(clf, X_digits, Y_digits, cv = 10)
print(scores.mean())
for i in scores:
	print("Value:", i)

