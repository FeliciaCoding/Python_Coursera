hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error,please enter numeric digits")
    quit()

def rug(h, r):
    rp= h*r
    ## print('rp')
    return rp

def opt(h,r):
    optp= 40*r+(h-40)*r*1.5
    return optp

if 0<=h<=40:
    p= rug(h, r)
    print('Pay:',p)

elif h>40:
    p=opt(h,r)
    print('Pay:',p)
else:
    print('Error')

#p = computepay(h,r)
#print(p)
##print("Pay", p)

hrs = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error,please enter numeric digits")
    quit()

def rcomputepay(h, r):
    if 0<=h<=40:
        p= h*r
        return p
    elif h>40:
        p = 40*r+(h-40)*r*1.5
        return p
    else:
        print('Error')

pay = rcomputepay(h, r)
print('Pay', pay)

#######錯誤
