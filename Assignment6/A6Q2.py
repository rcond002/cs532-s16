import tweepy
import xlsxwriter
import urllib.request
from bs4 import BeautifulSoup 

ckey = 'njD0kW0BVIIzixHVJ1aFuiTpF'
csecret = 'gBCbfupgnbJ2Sx23g6DlpsX6sTSATE31mBiM24pAeVwOIhHICC' 
atoken = '435458877-XQYTGqw7BoIxVjn7Al8hvefzcCMxtRLtfrBmltmd' 
asecret = 'XOf0GJxiYiWRslfjT1XRB9UHVQ3maXckLeTeUiBgQ5NOK'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

snames = []
anames = []
genders = []
count = 0

#filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\List.txt"
filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\Actual_Names.txt"
infile = open(filename, 'r')
for line in infile:
	snames.append(line)
print(len(snames))

#get actual name
for person in snames:
	user = api.get_user(person)
	#print(str(user.name).encode('utf-8'))
	anames.append(str(user.name))
print(len(anames))
print(len(followers))

#get gender
for person in snames:
	file = r"https://api.genderize.io/?name="+person
	try:
		response = urllib.request.urlopen(file)
		soup = BeautifulSoup(response, 'html.parser')
		for line in soup:
			if 'female' in line:
				print('female')
				genders.append('female')
			elif 'male' in line:
				print('male')
				genders.append('male')
			elif 'null' in line:
				print('null')
				genders.append('null')
	except:
		print(person)
print(len(genders))	

filename = r"C:\Users\Ryan\Documents\WebScience\Assignment6\Gender.txt"
outfile = open(filename, 'w')
outfile.write("\n".join(genders))
outfile.close()

filename2 = r'C:\Users\Ryan\Documents\WebScience\Assignment6\Gender_Table.xlsx'
workbook = xlsxwriter.Workbook(filename2)
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold' : 1})

#data headers
worksheet.write('A1', 'Names', bold)
worksheet.write('B1', 'Gender', bold)

row = 1
col = 0

#throw data into 
for name in anames:
	worksheet.write_string(row, col, name)
	row += 1

row1 = 1
col1 = 1	
for type in genders:
	worksheet.write_string(row1, col1, type)
	row1 += 1
	
workbook.close()
	
print("Done")



