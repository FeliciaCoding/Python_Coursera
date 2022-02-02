import urllib.request, urllib.parse, urllib.error

fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fh:
    print(line.decode().strip())

# >> But soft what light through yonder window breaks
#   It is the east and Juliet is the sun
#   Arise fair sun and kill the envious moon
#   Who is already sick and pale with grief
