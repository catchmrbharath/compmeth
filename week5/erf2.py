from scipy import *
from matplotlib.pyplot import *
import scipy.special as sp
ans = []
def func(x):
    return 2*exp(-x*x)/pi**0.5
x = linspace(0,1,1000)
y = func(x)
plot(x,y,'k')
N = 1200
y = []
for i in range(1,20):
    N = 2**i
    x = rand(2,N)
    x[1,:]*=2
    a = where (func(x[0,:])>x[1,:])
    ans =(shape(a)[1]/double(N))*2
    y.append(abs(ans-sp.erf(1)))
figure(2)
loglog(2**(arange(1,20)),y,'k')
show()
