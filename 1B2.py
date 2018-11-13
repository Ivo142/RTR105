import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
import numpy
from numpy import *  #Importē skaitlisko metožu funkcijas
x = linspace(0, 4)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
y1 = x
plt.plot(x, y1, color = "#464241")
y2 = x- x*x*x/(1*2*3)
plt.plot(x, y2, color = "#189156")
y3 = x- x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5)
plt.plot(x, y3, color = "#189126")
y4 = x- x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5) + x*x*x*x*x*x*x/(1*2*3*4*5*6*7)
plt.plot(x, y4, color = "#198456")

plt.show()






