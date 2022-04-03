# Error: Dont name the file "xml.py"

import xml.etree.ElementTree as ET

# data / a string
data = '''
<person>
    <name>Chunk</name>
    <phone type ="intl">
        +1 234 567 8899
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) # may blow up if there is a mistake in data above
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
