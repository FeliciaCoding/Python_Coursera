# write a Python program that expands on http://www.py4e.com/code3/urllinks.py
# use urllib to read the HTML from the data files
# extract the href= vaues from the anchor tags
# scan for a tag that is in a particular position relative to the first name in the list
# follow that link and repeat
# report the last name you find.


# Step 1: write the import lines
# Do not hard code any values.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# The user prompts for url/count/position

# url = 'http://py4e-data.dr-chuck.net/known_by_Marie.html'
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

url = input('Enter URL:')
count = int(input('Enter count:')) # error:float()
position = int(input('Enter position:'))-1


# Counting loop exactly like Blastoff!
for i in range(count): # range(start, stop[, step]) >> 0 1 2 3 4 >> Using a for loop with range(), we can repeat an action a specific number of times.
    # # Add the html=/soup=/tags= lines to the Blastoff! loop.
    # Do not change these lines at all.
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a') # a list of anchors
    # Take the index position of tags.
    tag = tags[position] # specific tag
    # .get() the url
    url = tag.get('href',None) # string is mutable
    # print the url
    print('Retrieving:', url)
# print the head
print(tag.contents[0]) # head


#for tag in tags:
     #hrefs = tag.get('href', None)
     #hreflist.append(hrefs)
     #html = urllib.request.urlopen(hreflist[real_position],context = ctx).read()
     #print('Retrieving:',hreflist[real_position])
     #counts = counts + 1
     #if counts == countf:
        #break


#for tag in tags:
    #hrefs = tag.get('href', None)
    #hreflist.append(hrefs)
    # ERROR : urls[3] NOT WORKING
#for urls in hreflist:
    #html = urllib.request.urlopen(hreflist[real_position],context = ctx).read()

    #print('Retrieving:',hreflist[real_position])
    #counts = counts + 1
    #if counts == countf:
        #break

#print(hreflist)

# print the url
