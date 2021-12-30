# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list
# if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# function to get unique value
###def unique(list):
    # initialize a null list
    ###unique_list = []
    # traverse for all element
    ###for line in list:
        #check if exists in unique_list or not
        ###if not line in unique_list
            ###unique_list.append(line)
    # print list
    ###for line in unique_list:
        ###print unique_list


# open the file and access to read
fh = open('romeo.txt')
#  error: read the file, turning into string
            # inp = fh.read()
# Call file.read() to return the entire content of file as a string.
##str= fh.read()
##print(str)

# build a list
lst = list()
# traverse elements
for line in fh:
    # delete extra n/
    line = line.rstrip()
    # turn string/line into lists
        ##!!!! dont use value as x
    words = line.split()

    ###print(words)

    ## Error: words are 4 lists, dont use < for  "list" in 'list ' >
    ##         if words in lst: continue
    ##         else: unique_list = lst.append(words)

    ## Error: conditions stay in the for loop
    ##        it will run 1 line and start to select words
    ##        instead of run every lines together and then select words


    # condition
        # name elements in the lists 'words' as "word"
    for word in words:  # make sure it is 'string' in 'list'
        if word not in lst:
            lst.append(word)
            lst.sort()
print(lst)

# Error : print(lst.sort())
#    bcs: printing value returned by sort() and sort() does not return anything.

    # print
    ##print(uniq_lst)

# sort and print the list
##sort(unique(value))
