grade = input('Enter grade:')
try:
    fg = float(grade)
except:
    print('Error, please enter numeric input')
    quit()

if 1.0 >= fg >= 0.9:
    print('A')
elif 0.9 > fg >= 0.8:
    print('B')
elif 0.8 > fg >= 0.7:
    print('C')
elif 0.7 > fg >= 0.6:
    print('D')
elif 0 <= fg < 0.6:
    print('F')
else:
    print('Error')
