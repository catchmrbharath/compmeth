from scipy import *
from matplotlib.pyplot import *
import scipy.weave as weave
from week0 import polint

def fourierSum(x):
    sum = 0.0
    a = -1
    for  i in range(1,11):
        sum = sum +(a*cos(i*x))/(i*i) 
        a*=-1
    return sum
def MaxError(n):
    x = linspace(0,2*math.pi,40)
    f = array(map(fourierSum,x))
    print f
    xx = linspace(0,2*math.pi,999)
    z = polint(x,f,xx,n)
    yy = z[0]
    dy = z[1]
    yacc = array(map(fourierSum,xx))
    return abs(yacc-yy).max()

x = linspace(0,2*math.pi,40)
f = array(map(fourierSum,x))
xx = linspace(0,2*math.pi,999)
z = polint(x,f,xx,5)
yy = z[0]
dy = z[1]
figure(0)
plot(xx,yy,'ro')
yacc = map(fourierSum,xx)

figure(1)
plot(xx,abs(dy),'k')

n = range(3,21)
maxArray = map(MaxError,n)
figure(2)
loglog(n,maxArray,'k')
show()

