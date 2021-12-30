# who has sent the greatest number of mail messages

#read through the mbox-short.txt
fh = open('mbox-short.txt')

# Error: read() create ONE String
#str= fh.read()
#str= str.rstrip()
#print(str)

# creates a Python dictionary
address = dict()

# looks for 'From ' lines
for line in fh:
    line = line.rstrip()

    if line.startswith('From '):
        #  takes the second word of those lines as the person who sent the mail
        words = line.split()
        email = words[1]
        #print(email)

        #   count of the number of times they appear in the file
        address[email] = address.get(email,0)+1
#print('Senders:',address)


#using a maximum loop to find the most prolific committer.
bigcount= None
bigword=None
for k,v in address.items():
    if bigcount is None or v>bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)
