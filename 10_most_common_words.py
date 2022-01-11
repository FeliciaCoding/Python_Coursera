# the top 10 most common words

fhand=open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
## complete dictinary called "counts"

# Important: even shorter version to replace below:
#   print(sorted([(v,k) for k,v in c.items()]))
# List comprehension: an expression as a list




list1=list()
for k, v in counts.items(): # dictionary >> tuples
    list1.append((v,k)) # reorder and add to a list

list1 = sorted(list1, reverse=True) # sort backward: highest to lowest value
# print(list1)
# [(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft'), (1, 'sick'), (1, 'pale'), (1, 'moon'), (1, 'light'), (1, 'kill'), (1, 'grief'), (1, 'fair'), (1, 'envious'), (1, 'east'), (1, 'breaks'), (1, 'already'), (1, 'Who'), (1, 'Juliet'), (1, 'It'), (1, 'But'), (1, 'Arise')]

for val, key in list1[:10]:
    print(key, val)

## breif version:
print(sorted([(v,k) for k,v in counts.items()], reverse=True))
#the 3
#is 3
#and 3
#sun 2
#yonder 1
#with 1
#window 1
#what 1
#through 1
#soft 1

## breif version:
print(sorted([(v,k) for k,v in counts.items()], reverse=True))

#>>[(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft'), (1, 'sick'), (1, 'pale'), (1, 'moon'), (1, 'light'), (1, 'kill'), (1, 'grief'), (1, 'fair'), (1, 'envious'), (1, 'east'), (1, 'breaks'), (1, 'already'), (1, 'Who'), (1, 'Juliet'), (1, 'It'), (1, 'But'), (1, 'Arise')]
