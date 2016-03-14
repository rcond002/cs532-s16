import tweepy

ckey = 'njD0kW0BVIIzixHVJ1aFuiTpF'
csecret = 'gBCbfupgnbJ2Sx23g6DlpsX6sTSATE31mBiM24pAeVwOIhHICC' 
atoken = '435458877-XQYTGqw7BoIxVjn7Al8hvefzcCMxtRLtfrBmltmd' 
asecret = 'XOf0GJxiYiWRslfjT1XRB9UHVQ3maXckLeTeUiBgQ5NOK'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

names = []
followers = []
count = 0
for user in tweepy.Cursor(api.friends).items(50):
	try:
		#print(count)
		print(user.screen_name)
		names.append(str(user.screen_name))
		process_status(user)
		count+=1
	except:
		pass
		count+=1
print(len(names))
print(len(followers))

filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\List.txt"
outfile = open(filename, 'w')
outfile.write("\n".join(names))
outfile.close()
filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\List1.txt"
outfile = open(filename, 'w')
outfile.write("\n".join(names))
outfile.close()

filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\List.txt"
infile = open(filename, 'r')
names = []
names1 = []

for line in infile:
	names.append(line)
print(len(names))

filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\List1.txt"
infile1 = open(filename, 'r')
for line1 in infile1:
	names1.append(line1)
print(len(names1))


for person in names:
	for peeps in names1:
		if person == peeps:
			pass
		else:
			#statement = api.exists_friendship(person, peeps)
			#print(statement)
			relationship = api.show_friendship(source_screen_name=person, target_screen_name=peeps)
			source, destination = relationship
			print(source.followed_by, destination.screen_name)
			print(destination.followed_by, source.screen_name)
			print("\n")
			if source.followed_by == true:
				filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\Relationships\'"+source.screen_name + ".txt"
				outfile = open(filename, 'a')
				outfile.write(source.screen_name + " "+str(source.followed_by) +" "+ destination.screen_name+"\n")
				outfile.close()