count=dict()
line=input('Enter a line of text:')

words = line.split()
print('Words:',words)

print('Counting...')
# dic goes thru keys while list goes thru values
for word in words: # elements in list
    count[word] = count.get(word,0)+1

print('Counts', count)
# count : dictionary
# count[word] : quantities / numbers
