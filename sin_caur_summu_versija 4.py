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

k = 0
a = (-1)**0*x**1/(1)
S = a
print ("a0 = %6.2f S0 = %6.2f"%(a,S))

k = 1
a = a * (-1)*x*x/((2*k)*(2*k + 1))
#S1 = (a0) + a1
#S1 = S0 +a1
S= S + a
print ("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

k = 2
a = a * (-1)*x*x/((2*k)*(2*k + 1))
#S1 = (a0 + a1) + a2
#S1 = S1 +a2
S =S + a
print ("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

k = 3
a = (-1)*x*x/((2*k)*(2*k + 1))
#S1 = (a0 + a1 +a2) + a3
#S1 = S2 +a3
S = S + a
print ("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))




