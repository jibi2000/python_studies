p=float(input('Enter Principle Amount'))
r=float(input('Enter Rate '))
t=float(input('Enter Time Period'))
si=p*r*t/100
ta=p+si
print("\n the simple intrest is {} and the total is {}".format(si,ta))