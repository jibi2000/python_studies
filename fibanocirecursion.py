def fib(n,a,b,c):
    c=a+b
    print(c)
    a=b
    b=c
    if (c < n):
        fib(n,a,b,c)
fib(30,-1,1,0)