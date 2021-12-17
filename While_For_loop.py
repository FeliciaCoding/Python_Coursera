# while loop: indefinite loop
i = 1
while i < 6:
  print(i)
  i += 1
# How many time it runs the loop?
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
# Finding Smallest number
smallest = None
print('before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

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


## my coding
#n = input('Enter a number / done')

#try:
    #if fn = float(n)
    #else n = done
#except:
    #print('Invalid input')

#while fn is True:
    #print(fn)

    #total= n
    #count = n
