import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
  # Parse the feed
  d=feedparser.parse(url)
  wc={}
  entrytitle ={}
  # Loop over all the entries
  for e in d.entries:
    if 'summary' in e: summary=e.summary
    else: summary=e.description
	
    entrytitle.append(e.title.encode('utf-8'))
    # Extract a list of words
    words=getwords(e.title+' '+summary)
    for word in words:
      wc.setdefault(word,0)
      wc[word]+=1
  return entrytitle,wc

def getwords(html):
  # Remove all the HTML tags
  txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
  return [word.lower() for word in words if word!='']


apcount={}
wordcounts={}
#filename1 = r"C:\Users\Ryan\Documents\WebScience\Assignment8\RSS.txt"
#filename1 = r"http://theworldsfirstinternetbaby.blogspot.com/feeds/posts/default?max-results=100&alt=rss"
feedlist=[]
#for line in open(filename1):
feedlist.append("http://theworldsfirstinternetbaby.blogspot.com/feeds/posts/default?max-results=100&alt=rss")


for feedurl in feedlist:
  try:
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word,count in wc.items():
      apcount.setdefault(word,0)
      if count>1:
        apcount[word]+=1
  except:
    print('Failed to parse feed %s' % feedurl)
print(len(apcount))

wordlist=[]
#get 500 words in the range
for w,bc in apcount.items():
  frac=float(bc)/len(feedlist)
  if len(wordlist) <= 500:
    #if frac>0.05 and frac<0.99:
    wordlist.append(w)   
print(len(wordlist))
	
filename2 = r"C:\Users\Ryan\Documents\WebScience\Assignment10\blogdata2.txt"
out=open(filename2,'a')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
  try:
    print(str(blog))
    out.write(str(blog))
  except:
    out.write(str(blog.encode('utf-8')))
  for word in wordlist:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')