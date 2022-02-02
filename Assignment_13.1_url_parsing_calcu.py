import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/comments_42.html
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
digi = []
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    num =  tag.contents[0]
     #print(tag.contents[0])
        #>>97
        #  97
        #  90
        #  90

    # print(tag.contents)
        #>> ['97']
        #   ['97']
        #   ['90']
        #   ['90']
        #   ['88']
        #   ['87']
        #   ['87']

    numf = float(num)
    digi.append(numf)
    count = count + 1

print('Sum:', sum(digi))
print('Count:', count)
