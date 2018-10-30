# -*- coding: utf -8 -*-
from math import sin
# a0, a1, a2, a3 -> a
# S0, S1, S2, S3 -> S
# (1.) * (2) = (2.) - float * int = float
# (1.) * (2.)= (2.) - float * float = float
# float(input())  -> float
x =float(input("Lietotāj, lūdzu ievadi argumentu (x): "))
#print type(x)

y = sin(x)
print ("sin(%.2f) = %.2f"%(x,y))

a = (-1)**0*x**1/(1)
S = a
print ("a = %.2f S0 = %.2f"%(a,S))

a = a * (-1)*x*x/(2*3)
#S1 = (a0) + a1
#S1 = S0 +a1
S= S + a
print ("a = %.2f S0 = %.2f"%(a,S))

a = a * (-1)*x*x/(4*5)
#S1 = (a0 + a1) + a2
#S1 = S1 +a2
S =S + a
print ("a = %.2f S0 = %.2f"%(a,S))

a = (-1)*x*x/(6*7)
#S1 = (a0 + a1 +a2) + a3
#S1 = S2 +a3
S = S + a
print ("a = %.2f S0 = %.2f"%(a,S))




