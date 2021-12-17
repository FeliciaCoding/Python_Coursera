# Write a program which repeatedly reads numbers until user enters"done"
# Once " done" is entered, print out the total, count, average of the numbers
# detected mistakes using try and except, print an error message and skip to the next number
num = 0 # iteration variables for count
tot = 0.0 # iteration variables for total
# write a loop : infinite loop
while True:
    sval = input('Enter a number:')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print('ALL DONE')
print(tot, num, tot/num)

# repeatedly prompts a user for integer numbers until the user enters 'done'.
# 'done' is entered, print out the largest and smallest of the numbers
# put out an appropriate message and ignore the number when users type an appropriate message.

#>> set iteration variables
min = None
max = None
# >> indefinite loop 
while True: # done forget :
    sval = input('Enter a numer:') # indent
    if sval == 'done':
        break
    try:
        ival = int(sval) # int() for integer, float for 小數
    except:
        print('Invalid input')
        continue

    if min is None :
        min = ival
    elif min > ival :
        min = ival

    if max is None :
        max = ival
    elif max < ival :
        max = ival

print('Maximum is', max)
print('Minimum is', min)
