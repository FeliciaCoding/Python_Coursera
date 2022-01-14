# The basic outline of this problem is to read the file,
# look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#converting the extracted strings to integers
# summing up the integers.



import re

fh = open('regex_sum_1414071.txt')

tot = 0

for line in fh:
    line = line.rstrip()
    num = re.findall('[0-9]+', line) # return lists

    for i in num:  # for i in the list of "num"
        inte = int(i) # turn string into integers

        tot = tot + inte
print('Sum:', tot)


# print(num)
#[]
#[]
#[]
#[]
#[]
#[]
#[]
#[]
#[]
#[]
#['817', '5172', '8321']
#[]
#['4188']
#[]
#['1525', '802']
#[]
#['3414', '8671']


# concise version
#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
