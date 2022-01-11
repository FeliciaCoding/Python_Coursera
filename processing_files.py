## to "read" the whole file
fhand = open('mbox-short.text')
inp = fhand.read()
# show how many cherecters using len()
print(len(inp))
>>> 94625 cherecter
# print the slices
print(inp[:20])

## search through a file
fhand = open('file.text')
for line in fhand:
    if line startswith('From: '):
        line = lint.rstip()
        #否則print（）會自己產生尾段n/，而原本就有一個n/就會多一行空白
        print(line)

## another way
fhand = open('file.text')
for line in fhand:
    line = lint.rstip()
    if not startswith('From: '):
    # if not 'xxx' in line
        continue # skip lines
    print(line)

## prompt for film name: counting certain words in a file
fname= input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
            count= count+1
print('There were', count, 'subject lines in', fname)

## Bad file fname
fname= input('Enter the file name:')
try:
    fhand= open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count=0
for line in fhand:
    if line startswith('Subject:'):
        count = count+1
print('There were', count, 'subject lines in', fname)
