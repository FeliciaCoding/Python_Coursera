#>>>>> 1st answer
# open the file and access to read
fh = open('romeo.txt')

# Call file.read() to return the entire content of file as a string.
str= fh.read()
str=str.rstrip()
##print(str)
words = str.split()
## print(words)

# build a list
lst = list()

# condition
for word in words:
    if not word in lst:
        lst.append(word)
        lst.sort()
print(lst)








#>>>>> 2nd answer
# open the file and access to read
fh = open('romeo.txt')

# build a list
lst = list()

# traverse elements
for line in fh:
    # delete extra n/
    line = line.rstrip()
    # turn string/line into lists

    words = line.split()

    # condition

    for word in words:
        if not word in lst:
            lst.append(word)
            lst.sort()
print(lst)
