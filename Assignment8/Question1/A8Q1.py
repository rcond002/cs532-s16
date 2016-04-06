from bs4 import BeautifulSoup 
import urllib.request 
	
count = 1
link = r"http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"	
while count < 100:
	print(count)
	response = urllib.request.urlopen(link)
	print(response.geturl())
	soup = BeautifulSoup(response, 'html.parser')
	#print(tag)	
	filename1 = r"C:\Users\Ryan\Documents\WebScience\Assignment8\Blogs.txt"
	outfile = open(filename1, 'a')
	temp = response.geturl()
	temp1 = temp[0:len(temp)-17]
	outfile.write(str(temp1))
	outfile.write("\n")
	outfile.close()
	
	for tag in soup.findAll('link'):	
		filename2 = r"C:\Users\Ryan\Documents\WebScience\Assignment8\Response.txt"
		outfile = open(filename2, 'w')
		outfile.write(str(tag.encode('utf-8')))
		outfile.write("\n")
		outfile.close()
			
		for line in open(filename2):
			if "application/rss+xml" in line:
				filename3 = r"C:\Users\Ryan\Documents\WebScience\Assignment8\RSS.txt"
				outfile = open(filename3, 'a')
				outfile.write(str(temp1)+"feeds/posts/default?alt=rss")
				outfile.write("\n")
				outfile.close()

	count+= 1
	

