import xlsxwriter

names= []
friends = []
filename = r"C:\Users\Ryan\Documents\WebScience\Assignment4\mln.graphml"
text = open(filename, 'r')
word= "name"
word2= "friend_count"
word3 = "mutual_friend_count"
count = 0
temp = 0
for line in text:
	if word in line:
		count += 1
		#print(line[27:len(line)-11])
		if count > 18:
			names.append(line[27:len(line)-11])
		elif count < 18:
			pass
	if word2 in line:
		if temp < 1:
			pass
			temp +=1
		else:
			if word3 in line:
				pass
			else:
				#print(line[35:len(line)-11])
				friends.append(int(line[35:len(line)-11]))
names.append("Michael Nelson")
friends.append(int(len(friends)))

count = 0
for name in names:
	print(name, friends[count])
	count += 1
print("number of friends:", len(friends))
print("number of names:", len(names))

filename2 = r'C:\Users\Ryan\Documents\WebScience\Assignment4\Table1.xlsx'
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
for Number in friends:
	worksheet.write_number(row1, col1, Number)
	row1 += 1
	
workbook.close()

