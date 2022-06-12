from sympy import *
n=int(input("n:"))
print(fibonacci(floor(log(bell(n+1),2))+1))