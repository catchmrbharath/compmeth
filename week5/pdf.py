
from scipy import *
from matplotlib.pyplot import *
import scipy.special as sp
def invsig(x):
    inv = []
    for i in range(len(x)):
        if(x[i]>pi):
            inv.append(0.0)
        else:
            inv.append(1.0)
    return array(inv)

def func(x):
        return ((1+cos(x))/pi)*invsig(x)

def comp(x):
    return (3.5-x)/5.0

def inverse(x):
    return (7.0-sqrt(49-40*x))/2.0
def scaledrand(x):
    return x*rand()
            
A = 1.225
N = 200000
randarea = A*rand(1,N)[0,:]
x1 = map(inverse,randarea)
x1 = array(x1)
fx = map(comp,x1)
y1 =map(scaledrand,fx) 

a = where ( func(x1[:])>y1[:])
xfinal = x1[a]
hist(xfinal,100)
show()


x = linspace(0,pi,200)
y = func(x)
plot(x,y,'k')


