n=input('Enter The Number Which u Wa to check Armstrong Number')
s=0
for i in n:
    i=int(i)
    s=s + i*i*i
    
if n == str(s):
    print('The number is armstrong')
else:
    print('it is not armstrong number')