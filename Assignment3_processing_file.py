##Write a program that prompts for a file name,
##then opens that file and reads through the file,
##and print the contents of the file in upper case.
##Use the file words.txt to produce the output below.

#My answer
fname = input('Enter a file name:')
try:
    fhand = open(fname) #access to file

except:
    print('File does not exist')
    quit()

# for lx in fhand
inp = fhand.read() # read file
for line in inp: # 不能放fname
    line = line.rstrip()

# variables.upper() =! strings.capitalize()
print(inp.upper())# withiut indent, 不能放fname/line

# Prof's answer

fname = input('Enter a file name:')
try:
    fhand = open(fname) #access to file

except:
    print('File does not exist')
    quit()

for lx in fhand:
    ly=lx.rstrip()
    print(ly.upper())


# Another example
fh = open('words.txt')
# print(fh) #>>> only show objects

if lx in fh:
    ly = lx.rstrip() # eliminate n/
    print(ly.upper()) # print lines / content


#>>>> my failed answer1 >> only print the last line in cap
fname = input('Enter a file name:')
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()

# 沒有放read file>> only open but not read
for line in fname:
    line = line.rstrip()

print(line.upper()) # put 'line' instead of 'inp'


#>>>>my failed answer2
fname = input('Enter a file name:')
try:
    fhand = open(fname) #access to file

except:
    print('File does not exist')
    continue / break >> using in  loop
inp = fhand.read() # read file
for line in inp: # 不能放fname
    line = line.rstrip()

print(inp.upper())# 不能放fname / fhand


# my faiiled answer 3
fname = input('Enter a file name:')
try:
    fhand = open(fname)

except:
    print('File does not exist')
    quit()

for line in fhand:
    line = line.rstrip()

print(line.upper())
## >>> output: AND MIND-NUMBING

# failed answer 4
fname = input('Enter a file name:')
try:
    fhand = open(fname)

except:
    print('File does not exist')
    quit()

for line in fhand:
    line = line.rstrip()

print(fhand.upper())
#>> traceback on line 103   print(fhand.upper())
##  AttributeError: '_io.TextIOWrapper' object has no attribute 'upper'
