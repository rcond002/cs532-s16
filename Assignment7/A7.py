
def getRecommendedItems(prefs,itemMatch,user):
	userRatings = prefs[user]
	scores={}
	totalSim={}
	
	#Loop over items rated by this user
	for (item,rating) in userRatings.items():
		#Loop over items similar to this one
		for (similarity,item2) in itemMatch[item]:
		
			#Ignore if this user has already rated this item
			if item2 in userRatings: continue
			
			#Weighted sum of rating times similarity
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating
			
			#Sum of all the similarities
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity
		
	#Divide each total score by total weighting to get an average
	rankings = [(score/totalSim[item],item) for item,score in scores.item( )]
		
	#Return the rankings from highlest to lowest
	rankings.sort()
	rankings.reverse()
	return rankings
	
def Movie(prefs, userid):
	userRatings = prefs[userid]
	favorite={}
	least={}
	
	for(item,rating) in userRatings.items():
		#print(item,rating)
		if int(rating) == 5.0:
			#print(item,rating)
			favorite[item]=rating
		if int(rating) == 1.0:
			#print(item,rating)
			least[item]= rating
		if len(least) < 3:
			if int(rating) == 2.0:
			#print(item,rating)
				least[item]= rating
		if len(favorite) < 3:
			if int(rating) == 4.0:
			#print(item,rating)
				favorite[item]= rating
			
	return favorite, least


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
		#print(id,age,gender,occupation,zipcode)
		if int(age) == 22:
			if gender == 'M':		
				if occupation == 'engineer':	
					count +=1
					print(id,age,gender,occupation)
					me[count]=id
		
	return me

def output(prefs):
	for (id,user) in person.items():
		favs, Less = Movie(prefs,user)
		for(item, rating) in favs.items():
			print(item,rating)
			filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\'"+user+"Fav.txt"
			outfile = open(filename, 'a')
			outfile.write(item +" "+str(rating))
			outfile.write("\n")
			outfile.close()
	#print(Less)
		for(item, rating) in Less.items():
			print(item,rating)
			filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\'"+user+"Least.txt"
			outfile = open(filename, 'a')
			outfile.write(item +" "+str(rating))
			outfile.write("\n")
			outfile.close()

prefs=loadMovieLens()
person = loadUsers()
output(prefs)