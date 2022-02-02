import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL:')
count = input('Enter count:')
countf = float(count)
position = input('Enter position:')
pi = int(position)

html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

counts = 0
tags = soup('a')
hreflist=list()
for tag in tags:
    hrefs = tag.get('href', None)
    hreflist.append(hrefs)
    link= hreflist[pi]
    counts = counts + 1

#print(hreflist)

    if counts <= countf:
        print(len(hreflist))
    else:
        break
