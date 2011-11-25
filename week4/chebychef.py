from numpy import *
from scipy import *
from matplotlib.pyplot import *

def chebcoef(a,b,func,n):
    bma = (b-a)/2
    bpa = (a+b)/2
    c = zeros((n,1))
    pikbyn = pi*linspace(0.5,n-0.5,n)/n
    y = cos(pikbyn)
    fn = func(y*bma + bpa)
    fac = 2.0/n
    for j in range(n):
        c[j] = sum(fn * cos(j*pikbyn))*fac
    return c



def chebev(x,c,a,b,n0):
    xx=x[where((x-a)*(x-b) <= 0)]
    z1 = (2*xx-a-b)/(b-a)
    z2 = 2*z1
    dd=zeros(z2.shape)
    d=zeros(z2.shape)
    for j in range(n0-1,0,-1):
        sv = d
        d = z2*d - dd + c[j]
        dd = sv
        y = z1*d - dd + 0.5*c[0]
    return y

def direct(x,c,a,b,n0):
    xx=x[where((x-a)*(x-b) <= 0)]
    z1 = (2*xx-a-b)/(b-a)
    z2 = 2*z1
    T = xx;Told=ones(xx.shape);y=0.5*c[0]*Told;
    for j in range(1,n0):
        y=y+c[j]*T
        Tnew=z2*T-Told
        Told=T
        T=Tnew
    return y

def f1(x):
    return exp(x)



def chebevCheck(a,b,f,n):
    c = chebcoef(a,b,f,n)
    figure(0)
    semilogy(range(n),abs(c),"or");
    title(r"Chebyshev coefs ")
    xlabel("$n$")
    ylabel("$|c_n|$")

def chebevFit(f,n,c):
    x=linspace(-1,1,1000)
    y=chebev(x,c,-1,1,60)
    yy=direct(x,c,-1,1,30)
    figure(5)
    plot(x,f(x),"k",x,y,"r",x,yy,"g");
    legend([r"$function$","clenshaw","direct"])
    print "Max difference between Clenshaw and Direct=%g\n" % abs(y-yy).max()
    error = []
    for i in range(6,13,2):
        y=chebev(x,c,-1,1,i)
        figure((i-4)/2)
        plot(x,y-f(x),'or')
        error.append(abs(y-f(x)).max())
        title(r"Error when approximating with $%d$ coefs" % i)
        xlabel("$x$")
    figure(13)
    title(r"Error vs No. of coefficients");
    ylabel("$Error$")
    semilogy(range(6,13,2),error,'k')

def g(x):
    return 1/(x*x+25)

def h(x):
    a = cos(pi*x)*cos(pi*x)
    return 1/(a+25)
def u(x):
    return exp(-abs(x))
def v(x):
    return sqrt(x+1)
def f(x):
    return exp(x)
c = chebcoef(-1,1,h,200)
chebevFit(h,15,c)

chebevCheck(-1,1,h,200) 
show()
