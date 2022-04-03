import urllib.request, urllib.parse, urllib.error
import json

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
#url= 'http://py4e-data.dr-chuck.net/comments_1414076.json'

# Error: while true >> create infinited loop
url = input('Enter location: ')
try:
    # send request and open the the url
    uh= urllib.request.urlopen(url)
    print('Retrieving', url)
except:
    print('====Failed====')
    quit()

# read and decode to readable format
data=uh.read().decode()
print('Retriving', len(data), 'characters')


info=json.loads(data)
#Error: print('Count:', len(info)) # only counting list instead od dic

count = 0
total = 0
for item in info['comments']: # inside the list of comments
    value = item["count"]
    value = int(value)
    total = total + value
    count = count + 1
print('Count:', count)
print('Sum:', total)
