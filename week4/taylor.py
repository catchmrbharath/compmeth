

from numpy import *
from scipy import *
from matplotlib.pyplot import *
import scipy.integrate as integ
import scipy.integrate as integrate

def expTaylor(x,n):
    y = linspace(0.0,0.0,len(x))
    for i in range(n):
        y = y + (x**i)/factorial(i)
    return y
x = linspace(-1,1,20)
y = expTaylor(x,10)
print y
yexact = exp(x)
semilogy(x,abs(y-yexact),'k')
show()



