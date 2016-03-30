def loadMovieLens():
	#get Movie Titles
	movies = {}
	movie_type={}
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.item'):
		(id,title)= line.split('|')[0:2]
		movies[id] = title
		
	#get Movie Genres
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.item'):
		(id,title,date0, date1, url, unknown, action, adventure, animation, childrens, comedy, crime, documentary, drama,fantasy,FilmNoir,horror,musical,mystery,romance, scifi,thriller,war,western)= line.split('|')[0:46]
		#movies[id] = title
		#print((id,title,date0, date1, url, unknown, action, adventure, animation, childrens, comedy, crime, documentary, drama,fantasy,FilmNoir,horror,musical,mystery,romance, scifi,thriller,war,western))
		if int(action) == 1:
			movie_type[title]= 'action'
		elif int(adventure) == 1:
			movie_type[title]= 'adventure'
		elif int(animation) == 1:
			movie_type[title]= 'animation'
		elif int(comedy) == 1:
			movie_type[title]= 'comedy'
		elif int(crime) == 1:
			movie_type[title]= 'crime'
		elif int(drama) == 1:
			movie_type[title]= 'drama'
		elif int(fantasy) == 1:
			movie_type[title]= 'fantasy'
		elif int(mystery) == 1:
			movie_type[title]= 'mystery'
		elif int(thriller) == 1:
			movie_type[title]= 'thriller'
		elif int(scifi) == 1:
			movie_type[title]= 'scifi'
		elif int(western) == 1:
			movie_type[title]= 'western'
		elif int(war) == 1:
			movie_type[title]= 'war'
		
	
		
	#load data
	prefs = {}
	for line in open(r'C:\Users\Ryan\Documents\WebScience\Assignment7\ml-100k\ml-100k\u.data'):
		(user,movieid,rating,ts)=line.split('\t')
		prefs.setdefault(user,{})
		prefs[user][movies[movieid]]=float(rating)
		
	return prefs, movies, movie_type
	
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
	
def MoviesNotRated(prefs, movies, userid, movie_type):
	userRatings = prefs[userid]
	count = 0
	num = 0
	
	for(id, title) in movies.items():
		temp = 0
		for(item,rating) in userRatings.items():
			if title == item:
				temp = 1
				filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\AllRated.txt"
				outfile = open(filename, 'a')
				outfile.write(str(title) +" "+str(rating))
				outfile.write("\n")
				outfile.close()	
		for(name,genre) in movie_type.items():
			if title == name:
				if temp == 0:
					try:
						if genre == 'comedy':
							filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\AllRated.txt"
							outfile = open(filename, 'a')
							outfile.write(str(title) +" 2.0")
							outfile.write("\n")
							outfile.close()	
							temp = 0
						elif genre == 'action':
							filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\AllRated.txt"
							outfile = open(filename, 'a')
							outfile.write(str(title) +" 1.0")
							outfile.write("\n")
							outfile.close()	
							temp = 0
						elif genre == 'crime':
							filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\AllRated.txt"
							outfile = open(filename, 'a')
							outfile.write(str(title) +" 4.0")
							outfile.write("\n")
							outfile.close()	
							temp = 0
						elif genre == 'drama':
							filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\AllRated.txt"
							outfile = open(filename, 'a')
							outfile.write(str(title) +" 5.0")
							outfile.write("\n")
							outfile.close()	
							temp = 0
						else:
							filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\AllRated.txt"
							outfile = open(filename, 'a')
							outfile.write(str(title) +" 3.0")
							outfile.write("\n")
							outfile.close()	
							temp = 0
					except:
						pass
	
	print(len(movies))
	print(num)
	
def movie_type_notrated(prefs, movie_type, user):
	userRatings = prefs[user]
	action1 = 0
	adventure1 = 0
	animation1 = 0
	comedy1 = 0
	crime1 = 0
	drama1 = 0
	fantasy1 = 0
	mystery1 = 0
	thriller1 = 0
	scifi1 = 0
	western1 = 0
	war1 = 0
	
	action2 = 0
	adventure2 = 0
	animation2 = 0
	comedy2 = 0
	crime2 = 0
	drama2 = 0
	fantasy2 = 0
	mystery2 = 0
	thriller2 = 0
	scifi2 = 0
	western2 = 0
	war2 = 0
	for (id, name) in movie_type.items():
		for(item,rating) in userRatings.items():
			if id == item:
				if rating == 5.0:
					if name == 'action':
						action1+=1
					if name == 'adventure':
						adventure1+=1
					if name== 'animation':
						animation1+=1
					if name== 'comedy':
						comedy1+=1
					if name== 'crime':
						crime1+=1
					if name== 'drama':
						drama1+=1
					if name == 'fantasy':
						fantasy1+=1
					if name == 'mystery':
						mystery1+=1
					if name== 'thriller':
						thriller1+=1
					if name == 'scifi':
						scifi1+=1
					if name == 'western':
						western1+=1
					if name == 'war':
						war1+=1
				if rating <= 2.0:
					if name == 'action':
						action2+=1
					if name == 'adventure':
						adventure2+=1
					if name== 'animation':
						animation2+=1
					if name== 'comedy':
						comedy2+=1
					if name== 'crime':
						crime2+=1
					if name== 'drama':
						drama2+=1
					if name == 'fantasy':
						fantasy2+=1
					if name == 'mystery':
						mystery2+=1
					if name== 'thriller':
						thriller2+=1
					if name == 'scifi':
						scifi2+=1
					if name == 'western':
						western2+=1
					if name == 'war':
						war2+=1
			
	filename = r"C:\Users\Ryan\Documents\WebScience\Assignment7\favmovietypes.txt"
	outfile = open(filename, 'a')
	outfile.write("action " +str(action1) +" adventure"+str(adventure1))
	outfile.write("\n")
	outfile.write("animation " +str(animation1) +" comedy"+str(comedy1))
	outfile.write("\n")
	outfile.write("crime " +str(crime1) +" drama"+str(drama1))
	outfile.write("\n")
	outfile.write("fantasy " +str(fantasy1) +" mystery"+str(mystery1))
	outfile.write("\n")
	outfile.write("thriller " +str(thriller1) +" scifi"+str(scifi1))
	outfile.write("\n")
	outfile.write("war " +str(war1) +" western"+str(western1))
	outfile.write("\n")
	outfile.write("action " +str(action2) +" adventure"+str(adventure2))
	outfile.write("\n")
	outfile.write("animation " +str(animation2) +" comedy"+str(comedy2))
	outfile.write("\n")
	outfile.write("crime " +str(crime2) +" drama"+str(drama2))
	outfile.write("\n")
	outfile.write("fantasy " +str(fantasy2) +" mystery"+str(mystery2))
	outfile.write("\n")
	outfile.write("thriller " +str(thriller2) +" scifi"+str(scifi2))
	outfile.write("\n")
	outfile.write("war " +str(war2) +" western"+str(western2))
	outfile.write("\n")
	outfile.close()

prefs, movies, movie_type =loadMovieLens()
person = loadUsers()
movie_type_notrated(prefs, movie_type, '216')



for (id,user) in person.items():
	if int(user) == 216:
		MoviesNotRated(prefs, movies, user, movie_type)			
				