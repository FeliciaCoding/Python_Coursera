import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Access to url
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1414075.xml'
#url = input('Enter - ')


html = urllib.request.urlopen(url, context=ctx).read()
print(html.decode())
print('Retrieving:', len(html), 'cheracters')

#xml
tree =ET.fromstring(html)

# use an XPath selector string to look through the entire tree of XML for any tag named 'count'
lst = tree.findall('.//count')
    # Error: lst = tree.findall('comment/count') >> fund nothing
print('Count:', len(lst))
#   print(lst)
#>> [<Element 'count' at 0x105f5d900>, <Element 'count' at 0x105f4dc20>, <Element 'count' at 0x105f4dae0>, <Element 'count' at 0x105f4dd60>, <Element 'count' at 0x105f4d9a0>, <Element 'count' at 0x105f4d8b0>, <Element 'count' at 0x105f84e00>, <Element 'count' at 0x105f84ef0>, <Element 'count' at 0x10604b040>, <Element 'count' at 0x10604b130>, <Element 'count' at 0x10604b220>, <Element 'count' at 0x10604b310>, <Element 'count' at 0x10604b400>, <Element 'count' at 0x10604b4f0>, <Element 'count' at 0x10604b5e0>, <Element 'count' at 0x10604b6d0>, <Element 'count' at 0x10604b7c0>, <Element 'count' at 0x10604b8b0>, <Element 'count' at 0x10604b9a0>, <Element 'count' at 0x10604ba90>, <Element 'count' at 0x10604bb80>, <Element 'count' at 0x10604bc70>, <Element 'count' at 0x10604bd60>, <Element 'count' at 0x10604be50>, <Element 'count' at 0x10604bf40>, <Element 'count' at 0x10604f090>, <Element 'count' at 0x10604f180>, <Element 'count' at 0x10604f270>, <Element 'count' at 0x10604f360>, <Element 'count' at 0x10604f450>, <Element 'count' at 0x10604f540>, <Element 'count' at 0x10604f630>, <Element 'count' at 0x10604f720>, <Element 'count' at 0x10604f810>, <Element 'count' at 0x10604f900>, <Element 'count' at 0x10604f9f0>, <Element 'count' at 0x10604fae0>, <Element 'count' at 0x10604fbd0>, <Element 'count' at 0x10604fcc0>, <Element 'count' at 0x10604fdb0>, <Element 'count' at 0x10604fea0>, <Element 'count' at 0x10604ff90>, <Element 'count' at 0x1060540e0>, <Element 'count' at 0x1060541d0>, <Element 'count' at 0x1060542c0>, <Element 'count' at 0x1060543b0>, <Element 'count' at 0x1060544a0>, <Element 'count' at 0x106054590>, <Element 'count' at 0x106054680>, <Element 'count' at 0x106054770>]

total = 0
for item in lst:
    words = item.text
    y = int(words)
    total = total + y
print(total)
