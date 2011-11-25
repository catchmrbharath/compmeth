
from numpy import *
from scipy import *
from matplotlib.pyplot import *
import scipy.integrate as integ
import scipy.integrate as integrate
def fourierCoeff(func,n):
    
    coef = linspace(0,0,n)
    for i in range(n):
        shifted = lambda x: func(x-1)*cos(i*pi*x/2.0)
        temp = integrate.quad(shifted,0,2)
        coef[i] = temp[0]
        if(i==0):
            coef[i]/=2.0
     
    return coef
       

def fourierFit(x,coeff,n):
    y = linspace(0.0,0.0,len(x))
    for i in range(len(x)):
        for j in range(n):
            y[i]+=coeff[j]*cos(j*pi*x[i]/2.0)
    return y





    
def f(x):
    return exp(x)

def g(x):
    return 1/(x*x+25)

def h(x):
    a = cos(pi*x)*cos(pi*x)
    return 1/(a+25)
def u(x):
    return exp(-abs(x))
def v(x):
    return sqrt(x+1)
def plotFourier(f,n):
    c = fourierCoeff(f,n)
    a = range(len(c))
    semilogy(a,abs(c),'k')
    title("Coefficient magnitude vs coefficient number")
    x = linspace(0,2,100)
    y = fourierFit(x,c,20)
    xexact = linspace(-1,1,100)
    yexact = f(xexact)
    xshifted = x- [1]*len(x)
    figure(2)
    plot(xshifted,y,'k',color='g')
    plot(xexact,yexact,'k')
    legend(["fitted function","exact function"])
    figure(3)
    semilogy(xexact,abs(yexact-y),'k')
    title("Error distribution")
plotFourier(v,100)
show()

   
