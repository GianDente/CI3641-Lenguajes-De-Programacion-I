from sympy import *

n = int(input("Introduzca el valor de n:"))

print(fibonacci(floor(log(bell(n+1),2))+1))
