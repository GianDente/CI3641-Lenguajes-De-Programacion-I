from sympy import *
import sys
n=int(sys.argv[1])
print(fibonacci(floor(log(bell(n+1),2))+1))
