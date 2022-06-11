import math
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def Bell(n):
    if n==0:
        return 1
    elif n>0:
        sum=0
        for k in range(0,n):
            sum+=(fact(n-1)/(fact(n-1-k)*fact(k)))*Bell(k)
        return sum
def fib(n):
    if 0<=n<2:
        return n
    elif n>=2:
        return fib(n-1)+fib(n-2)
def evil(n):
    return fib(math.floor(math.log2(Bell(n+1)))+1)
n=int(input("Valor de n:"))
print(evil(n))