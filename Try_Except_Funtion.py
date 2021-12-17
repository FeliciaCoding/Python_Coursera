# 1
astr = 'Hello Felicia'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)
# 2
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
# 3
rawstr = input('Enter a number')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')

# Assignement
hrs = input('Enter hours')
fhrs = float(hrs)
##try:
    ##fhrs = float(hrs)
##except:
    ##fhrs = -1
##if fhrs < 0
    ##print('Not a number')
##else:

rate = input('Enter rate per hour')
frate = float(rate)
##try:
    ##frate = float(rate)
##except:
    ##frate = -1
##if frate < 0
    ##print('Not a number')
## gross_pay = float(hrs)*float(rate)
##gross_rate_above40 = float(hrs)*float(rate)*1.5
gross_pay = fhrs*frate
gross_rate_above40 = frate*40+frate*(fhrs-40)*1.5
if fhrs > 0:
    print(gross_rate_above40)
else:
    print(gross_pay)

# Answer
sh = inpit('Enter hours:')
sr= inpot('Enter rate:')
### Try to answer with non-digit to see if there are dangerious codes
### Find dangerous code to use function <try + except>
try :
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, please enter numeric input')
    quit() ## if it doesnt make sense, do not run the codes !

print (fh, fr)
if fh > 40:
    reg = fh * fr
    otp = (fh-40.0)* (fr*0.5)
    xp = reg + opt
else:
    xp = fh * fr
print('Pay:',xp)
