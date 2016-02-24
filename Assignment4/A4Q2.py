import tweepy
import xlsxwriter

ckey = 'njD0kW0BVIIzixHVJ1aFuiTpF'
csecret = 'gBCbfupgnbJ2Sx23g6DlpsX6sTSATE31mBiM24pAeVwOIhHICC' 
atoken = '435458877-XQYTGqw7BoIxVjn7Al8hvefzcCMxtRLtfrBmltmd' 
asecret = 'XOf0GJxiYiWRslfjT1XRB9UHVQ3maXckLeTeUiBgQ5NOK'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

names = []
followers = []
#for user in tweepy.Cursor(api.followers, screen_name="twitter").items():
count = 0
for user in tweepy.Cursor(api.friends, count = 200).items():
	try:
		#print(count)
		print(user.name, user.followers_count)
		names.append(str(user.name))
		followers.append(int(user.followers_count))
		process_status(user)
		count+=1
	except:
		pass
		count+=1
print(len(names))
print(len(followers))
#print(len(tweepy.Cursor(api.followers, screen_name="twitter").items()))

filename2 = r'C:\Users\Ryan\Documents\WebScience\Assignment4\Table2.xlsx'
workbook = xlsxwriter.Workbook(filename2)
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold' : 1})

#data headers
worksheet.write('A1', 'Name', bold)
worksheet.write('B1', 'Num of Friends', bold)

row = 1
col = 0

#throw data into 
for name in names:
	worksheet.write_string(row, col, name)
	row += 1

row1 = 1
col1 = 1	
for Number in followers:
	worksheet.write_number(row1, col1, Number)
	row1 += 1
	
workbook.close()