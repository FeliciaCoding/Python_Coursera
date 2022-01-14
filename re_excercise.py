import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x) #greedy
print(y)
#>> ['From: Using the :']
z = re.findall('^F.+?:', x) # ? non-greedy
print(z)
 #>> ['From:']

a = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
b = re.findall('\S+?@\S+', a) # non-blank mamytimes(non-greedy) @ non-blank mamytimes(greedy)
print(b)
#>> ['stephen.marquard@uct.ac.za']


c= re.findall([a-z0-9], a)
print(c)
