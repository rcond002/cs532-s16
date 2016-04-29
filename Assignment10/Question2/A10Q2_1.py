def readfile(filename):
  #lines=[line for line in file(filename)]
  lines=[]
  for line in open(filename):
    lines.append(line)
	
  # First line is the column titles
  colnames=lines[0].strip().split('\t')[1:]
  rownames=[]
  data=[]
  for line in lines[1:]:
    p=line.strip().split('\t')
    # First column in each row is the rowname
    rownames.append(p[0])
    # The data for this row is the remainder of the row
    data.append([float(x) for x in p[1:]])
  return rownames,colnames,data

def getwords(html):
  # Remove all the HTML tags
  txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
  return [word.lower() for word in words if word!='']
  
def getwordcounts(url, words):
  # Parse the feed
  d=feedparser.parse(url)
  wording = {}
  # Loop over all the entries
  for e in d.entries:
    wc={}
    if 'summary' in e: summary=e.summary
    else: summary=e.description
	
    # Extract a list of words
    temp=getwords(e.title+' '+summary)
    fulltext = temp
    for word in words:
      if word in fulltext:
		wc.setdefault(word,0)
		wc[word]+=1
    wording[e.title] = wc
  return wording
  
blognames,words,data=readfile(r'C:\Users\Ryan\Documents\WebScience\Assignment10\blogdata2.txt')
wordcounts={}
wording = getwordcounts(r"http://theworldsfirstinternetbaby.blogspot.com/feeds/posts/default?max-results=100&alt=rss", words)
wordcounts = wording

filename2 = r"C:\Users\Ryan\Documents\WebScience\Assignment10\blogdata3.txt"
out=open(filename2,'a')
out.write('Blog')
for word in words: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
  try:
    print(str(blog))
    out.write(str(blog))
  except:
    out.write(str(blog.encode('utf-8')))
  for word in words:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')