import math


def loadMovieLens():
	#get Movie Titles
	movies = {}
	favs = {}
	less={}
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.item'):
		(id,title)= line.split('|')[0:2]
		#Most Favs
		if str(title) == 'Billy Madison (1995)':
			favs[0]= title
		elif str(title) == 'Pulp Fiction (1994)':
			favs[1]= title
		elif str(title) == 'Shawshank Redemption, The (1994)':
			favs[2]= title
		elif str(title) == 'Ace Ventura: Pet Detective (1994)':
			favs[3]= title
		elif str(title) == 'Maverick (1994)':
			favs[4]= title
		#Least Favs
		elif str(title) == 'Terminator 2: Judgment Day (1991)':
			less[0]= title
		elif str(title) == 'Gone with the Wind (1939)':
			less[1]= title
		elif str(title) == 'Aliens (1986)':
			less[2]= title
		elif str(title) == 'Terminator, The (1984)':
			less[3]= title
		elif str(title) == 'Shining, The (1980)':
			less[4]= title
		movies[id] = title
		
	#load data
	prefs = {}
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.data'):
		(user,movieid,rating,ts)=line.split('\t')
		prefs.setdefault(user,{})
		prefs[user][movies[movieid]]=float(rating)
		
	return prefs, movies, favs, less
	
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
			
def getMean(prefs, movie1):
	mean1=0
	tot1 = 0
	count = 0
	for(user, movie) in prefs.items():
		userRatings = prefs[user]
		for (item, rating) in userRatings.items():
			if movie1 == item:
				#print(movie1,user,item,rating)
				count+=1
				tot1+= rating
	
	mean1= tot1/count
	#print(mean1)
	return mean1
	
def rvalue(mean1,mean2,prefs, movie1,movie2):
	r={}
	r=0
	top = 0
	bottomright = 0
	bottomleft = 0
	
	for(user, movie) in prefs.items():
		userRatings = prefs[user]
		for (item, rating) in userRatings.items():
			if movie1 == item:
				for(user1, move) in prefs.items():
					userRatings = prefs[user1]
					for (item1, rating1) in userRatings.items():
						if movie2 == item1:
							if user1 == user:
								top += (rating-mean1)*(rating1-mean2)
								bottomleft +=  (rating-mean1)*(rating-mean1)
								bottomright += (rating1-mean2)*(rating1-mean2)
	
	if bottomleft == 0 or bottomright == 0:
		r = 5
		return r
	else:
		r = top/(math.sqrt(bottomleft)*math.sqrt(bottomright))
		#print("R:",r)
		return r
	
prefs, movies, favs, less = loadMovieLens()
person = loadUsers()
mean1 = getMean(prefs, less[1])


for (id, title) in movies.items():
	mean2 = getMean(prefs, title)
	r =rvalue(mean1,mean2, prefs, less[1], title)
	print(r)
	if r > .50:	
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\'"+less[1]+" MostCorrelated.txt"
		outfile = open(filename, 'a')
		outfile.write("R: "+str(r)+" movie1: " + str(title))
		outfile.write("\n")
		outfile.close()
	elif r < -.50:
		filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\'"+less[1]+" LeastCorrelated.txt"
		outfile = open(filename, 'a')
		outfile.write("R: "+str(r)+" movie1: " + str(title))
		outfile.write("\n")
		outfile.close()