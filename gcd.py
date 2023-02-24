def gcd(a,b):
    c=a
    while(c != 0):
        c=a % b
        b=a
        a=c
    print(a)
gcd(150,35)
# print(150%35)
    