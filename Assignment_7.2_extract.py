#Write a program that prompts for a file name,
#then opens that file and reads through the file,
#looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
#Count these lines
#and extract the floating point values from each of the lines #
#and compute the average of those values and produce an output as shown below.
#Average spam confidence: 0.7507185185185187

# promp for file name : mbox-short.txt
# open file and access to read
fm = input('Enter a file name:')
fh = open(fm)

#fh = open('mbox-short.txt')

#Error: inp=fh.read() >> delete it, or it will trun into a giant string

# set iteration
count = 0
tot = 0
# initiate a list
list = list()
# traverse elements
for line in fh:
    # find lines: skip and find the targeted lines
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    # slice
    x = line.split()
    value = x[1]
    # append
    list.append(value)

    count = count+1

    ##value = float(line[mark+1:])

    # turn string into numbers
    fvalue = float(value)
    tot = tot + fvalue

avg = tot / count
print('Average spam confidence:', avg)
