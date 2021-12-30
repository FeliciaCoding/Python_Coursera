# Definite loops and dictionaries
jjj = {'chuck':1, 'fred':42, 'jan':100}

for key in jjj:
    print(key,jjj[key])

# get a list of keys
print(list(jjj))
print(jjj.keys())
# values/quantities
print(jjj.values())
# both keys and values
print(jjj.items())

# 2 iteration variable for keys and values (k and v )
for k,v in jjj.items():
    print(k,v)
