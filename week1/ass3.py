from numpy import *
from matplotlib.pyplot import *
import scipy.weave as weave
from week0 import polint
import scipy.special as  sp

def func_new (x):
    num = power(x,(1+sp.jv(0,x)))
    denom = sqrt(1-x*x)
    return num/denom

xbig = arange(0.1,0.95,0.05)
funcBigTable = array(map(func_new,xbig))
figure(0)
plot(xbig,funcBigTable,'k',color = 'g')

for n in range(3,8):
    x = linspace(0.3,0.7,n+1)
    y = map(func_new,x)
    z = polint(xbig,funcBigTable,x,n)
    figure(n)
    semilogy(x,abs(y-z[0]),'k')
show()
