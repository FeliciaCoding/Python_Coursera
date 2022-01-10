# sort tuples with values instead of keys

#dictionary
d = {'a':10, 'b':1, 'c':22}

# using list to sort
tmp = list()
# for loop to reorgainzed the order of v and k
for k,v in d.items():
    tmp.append((v, k))
print(tmp)
#>> [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)
# >> [(22, 'c'), (10, 'a'), (1, 'b')]
