# Modulo que define el tipo de los cuaterniones y operadores aritmeticos sobre estos.
# Giancarlo Dente
# 15-10395

import math

class Cuaternion(object):

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # definicion suma para los cuaterniones:
    def __add__(self, cuaternion2):
        if type(cuaternion2) == Cuaternion:
            return Cuaternion(self.a + cuaternion2.a, self.b + cuaternion2.b, self.c + cuaternion2.c, self.d + cuaternion2.d)
        elif type(cuaternion2 == int or cuaternion2 == float):
            return Cuaternion(self.a + cuaternion2, self.b + cuaternion2, self.c + cuaternion2, self.d + cuaternion2)
        else:
            pass

    # definicion conjugada para los cuaterniones:
    def __invert__(self):
        return Cuaternion( self.a, - self.b, - self.c, - self.d )


    # definicion producto para los cuaterniones:
    def __mul__(self, cuaternion2):
        if type(cuaternion2) == Cuaternion:
            return Cuaternion((self.a*cuaternion2.a) - (self.b*cuaternion2.b) - (self.c*cuaternion2.c) - (self.d*cuaternion2.d), 
                              (self.a*cuaternion2.b) + (self.b*cuaternion2.a) + (self.c*cuaternion2.d) - (self.d*cuaternion2.c), 
                              (self.a*cuaternion2.c) - (self.b*cuaternion2.d) + (self.c*cuaternion2.a) + (self.d*cuaternion2.b),
                              (self.a*cuaternion2.d) + (self.b*cuaternion2.c) - (self.c*cuaternion2.b) + (self.d*cuaternion2.a))
        elif type(cuaternion2 == int or cuaternion2 == float):
            return Cuaternion(self.a * cuaternion2, self.b * cuaternion2, self.c * cuaternion2, self.d * cuaternion2)
        else:
            pass

    # definicion medida o valor absoluto para los cuaterniones:
    def __neg__(self):
        return ( math.sqrt(self.a*self.a + self.b*self.b + self.c*self.c + self.d*self.d) )

    # Salida de los cuaterniones:
    def __str__(self):
        return ( f"{self.a} + {self.b}i + {self.c}j + {self.d}k" )
        

