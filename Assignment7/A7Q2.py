import math


def loadMovieLens():
	#get Movie Titles
	movies = {}
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.item'):
		(id,title)= line.split('|')[0:2]
		movies[id] = title
		
	#load data
	prefs = {}
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.data'):
		(user,movieid,rating,ts)=line.split('\t')
		prefs.setdefault(user,{})
		prefs[user][movies[movieid]]=float(rating)
		
	return prefs
	
def loadUsers():
	#get People
	me={}
	count = 0
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.user'):
		(id,age,gender,occupation,zipcode)= line.split('|')[0:5]	
		#print(id,age,gender,occupation)
		me[count]=id
		count+=1
		
	return me
	
def CorrelationTest(prefs, userid1, userid2):
	userRatings = prefs[userid1]
	userRatings1 = prefs[userid2]
	r={}
	meanuser1={}
	meanuser2={}
	tot1=0
	tot2=0
	mean1=0
	mean2=0
	r=0
	top = 0
	bottomright = 0
	bottomleft = 0
	
	#Calculate mean of user 1
	for(item,rating) in userRatings.items():
		tot1+= rating
	mean1= tot1/len(userRatings)
	#print("Mean1:",mean1)
	
	#Calculate mean of user 2
	for(item2,rating2) in userRatings1.items():	
		tot2+= rating2
	mean2= tot2/len(userRatings1)
	#print("Mean2:", mean2)
	
	for(item,rating) in userRatings.items():
		for(item2,rating2) in userRatings1.items():
			if item == item2:
				top += (rating-mean1)*(rating2-mean2)
				bottomleft +=  (rating-mean1)*(rating-mean1)
				bottomright += (rating2-mean2)*(rating2-mean2)
	
	if bottomleft == 0 and bottomright == 0:
		r = 5
		return r
	else:
		r = top/(math.sqrt(bottomleft)*math.sqrt(bottomright))
		print("R:",r)		
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\'"+user+"ID.txt"
		outfile = open(filename, 'a')
		outfile.write("R: "+str(r)+" user1: " + str(user1))
		outfile.write("\n")
		outfile.close()
			
	return r

prefs=loadMovieLens()
person = loadUsers()

#Determine Max and Min Correlation
for (id,user) in person.items():
	if int(user) == 216:
		for (id1,user1) in person.items():
			print(user,user1)
			if user == user1:
				pass
			else:
				r = CorrelationTest(prefs, user, user1)
				if r == 1.0:
					filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\MaxCorrelated.txt"
					outfile = open(filename, 'a')
					outfile.write(str(user1) +" "+str(r))
					outfile.write("\n")
					outfile.close()
				if r == -1.0:
					filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\LeastCorrelated.txt"
					outfile = open(filename, 'a')
					outfile.write(str(user1) +" "+str(r))
					outfile.write("\n")
					outfile.close()

#print(person)
#output(prefs)