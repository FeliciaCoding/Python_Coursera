fname = input('Enter a file name:')
try:
    fhand = open(fname) #access to file

except:
    print('File does not exist')
    quit()
inp = fhand.read() # read file
for line in inp: # 不能放fname
    line = line.rstrip()

# variables.upper() =! strings.capitalize()
print(inp.upper())# 不能放fname
