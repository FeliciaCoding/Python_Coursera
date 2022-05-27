# assignment_10.2_tuples_sort

# read through the mbox-short.txt
# figure out the distribution by hour of the day for each of the messages
# pull the hour out from the 'From ' line by finding the time
# splitting the string a second time using a colon.
#       From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# print out the counts, sorted by hour as shown
#04 3   06 1    07 1    09 2    10 3    11 6    14 1
#15 2   16 4    17 2    17 2    18 1    19 1

fn = input("Enter file name:")
try:
    fh = open(fn) # read thru
except:
    print('Error, Enter a valid file name')
    quit()


# fh = open('mbox-short.txt')

c = dict()


for line in fh:
    if not line.startswith('From '): # filter
        continue
    line=line.rstrip() # delete extra n/

    #   print(line.rstrip())
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
#From zqian@umich.edu Fri Jan  4 16:10:39 2008
#From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
#From zqian@umich.edu Fri Jan  4 15:03:18 2008
#From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008
#From cwen@iupui.edu Fri Jan  4 11:37:30 2008
#From cwen@iupui.edu Fri Jan  4 11:35:08 2008
#From gsilver@umich.edu Fri Jan  4 11:12:37 2008
#From gsilver@umich.edu Fri Jan  4 11:11:52 2008
#From zqian@umich.edu Fri Jan  4 11:11:03 2008
#From gsilver@umich.edu Fri Jan  4 11:10:22 2008
#From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008
#From zqian@umich.edu Fri Jan  4 10:17:43 2008
#From antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008
#From gopal.ramasammycook@gmail.com Fri Jan  4 09:05:31 2008
#From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008
#From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008
#From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008
#From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008
#From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008
#From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008
#From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008
#From ray@media.berkeley.edu Thu Jan  3 17:07:00 2008
#From cwen@iupui.edu Thu Jan  3 16:34:40 2008
#From cwen@iupui.edu Thu Jan  3 16:29:07 2008
#From cwen@iupui.edu Thu Jan  3 16:23:48 2008

    words = line.split()
    #print(words)
    # ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
    #['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008']
    #['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '16:10:39', '2008']
    #['From', 'rjlowe@iupui.edu', 'Fri', 'Jan', '4', '15:46:24', '2008']
    #['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '15:03:18', '2008']
    #['From', 'rjlowe@iupui.edu', 'Fri', 'Jan', '4', '14:50:18', '2008']
    #['From', 'cwen@iupui.edu', 'Fri', 'Jan', '4', '11:37:30', '2008']
    #['From', 'cwen@iupui.edu', 'Fri', 'Jan', '4', '11:35:08', '2008']
    #['From', 'gsilver@umich.edu', 'Fri', 'Jan', '4', '11:12:37', '2008']
    #['From', 'gsilver@umich.edu', 'Fri', 'Jan', '4', '11:11:52', '2008']
    #['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '11:11:03', '2008']
    #['From', 'gsilver@umich.edu', 'Fri', 'Jan', '4', '11:10:22', '2008']
    # etc......


    ## Error : add into a list>> Only ONE list, cannot extract time by positioning
    # list.append(words)
    # print(list)
    # >> \[['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008'], ['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '16:10:39', '2008'], ['From', 'rjlowe@iupui.edu', 'Fri', 'Jan', '4', '15:46:24', '2008'], ['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '15:03:18', '2008'], ['From', 'rjlowe@iupui.edu', 'Fri', 'Jan', '4', '14:50:18', '2008'], ['From', 'cwen@iupui.edu', 'Fri', 'Jan', '4', '11:37:30', '2008'], ['From', 'cwen@iupui.edu', 'Fri', 'Jan', '4', '11:35:08', '2008'], ['From', 'gsilver@umich.edu', 'Fri', 'Jan', '4', '11:12:37', '2008'], ['From', 'gsilver@umich.edu', 'Fri', 'Jan', '4', '11:11:52', '2008'], ['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '11:11:03', '2008'], ['From', 'gsilver@umich.edu', 'Fri', 'Jan', '4', '11:10:22', '2008'], ['From', 'wagnermr@iupui.edu', 'Fri', 'Jan', '4', '10:38:42', '2008'], ['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '10:17:43', '2008'],
    #    XXXXXXXXX       time = words[5]


    time = words[5]
    #print(time)
    #09:14:16
    #18:10:48
    #16:10:39
    #15:46:24
    #15:03:18
    #14:50:18
    #11:37:30
    #11:35:08
    # etc......


    hours = time.split(':')
    #print(hours)
    #['09', '14', '16']
    #['18', '10', '48']
    #['16', '10', '39']
    #['15', '46', '24']
    #['15', '03', '18']
    # etc......

    hours = hours[0]
    #print(hours)
    #09
    #16
    #15
    #15
    #14
    #11
    # etc......

    c[hours] = c.get(hours,0)+1
#print(c)
#{'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}

#WAY 1:  >> using list.sorted() to sort
#tmp= list()
#for k,v in c.items():
    #tmp.append((k, v))
    #tmp = sorted(tmp)
#print(tmp)
#[('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]

#WAY 2:  >> using sorted(dictionary.items()) = sorted(tuples)
t = sorted(c.items())

for k,v in t:
    print(k,v)
    #04 3
    #06 1
    #07 1
    #09 2
    #10 3
    #11 6
    #14 1
    #15 2
    #16 4
    #17 2
    #18 1
    #19 1

















    #Error: print(k,v)
    #09 2
    #18 1
    #16 4
    #15 2
    #14 1
    #11 6
    #10 3
    #07 1
    #06 1
    #04 3
    #19 1
    #17 2
