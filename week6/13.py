from matplotlib import *
from numpy import *
import scipy.special as sp

def sign(a,b):
    if(b>=0):
        return abs(a)
    else:
        return -abs(a)

def f(x):
    return sp.jv(0,x)

def f2(x):
    return sin(x)
def brentGoldenSearch(func, ax,bx,cx, tol):
    ITMAX = 100
    CGOLD = 0.3819669
    ZEPS = 1.0e-10
    iter = 0
    a=b=d=etemp=fu=fv=fw=fx=p=q=r=tol1=tol2=u=v=w=x=xm=0.0
    e = 0.0
    if ax<cx: a=ax 
    else:a=cx
    if ax>cx: b = ax 
    else: b = cx
    x =w =v= bx
    fw = fv= fx = func(x)
    for iter in xrange(1,ITMAX):
        xm = 0.5*(a+b)
        tol1 = tol*abs(x)+ZEPS
        tol2 = 2*tol1
        if(abs(x-xm)<= (tol2-0.5*(b-a))):
            return x,fx,iter
        if (abs(e)>tol1):
            r = (x-w)*(fx-fv)
            q = (x-v)*(fx -fw)
            p = (x-v)*q - (x-w)*r
            q = 2.0*(q-r)
            if(q>0):p = -p
            q = abs(q)
            etemp = e
            e = d
            if(abs(p)>=abs(0.5*q*etemp) or p<=q*(a-x) or p>=q*(b-x)):
                if x>=xm: temp = a-x
                else: temp = b-x
                e = temp
                d = CGOLD*e
            else:
                d = p/q
                u= x+d
                if u-a<tol2 or b-u <tol2:
                    d = sign(tol1,xm-x)
        else:
            if(x>=xm): e = a-x
            else: e = b-x
            d = CGOLD*e
        if(abs(d) >=tol1): u = x+d
        else:  u = x+sign(tol1,d)
        fu = func(u)
        if(fu<=fx):
            if(u>=x):a = x
            else: b = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u<x: a = u
            else: b = u
            if(fu<=fw or w==x):
                v =w
                w = u
                fv = fw
                fw = fu
            elif((fu<=fv or v==x) or v==w):
                v = u
                fv = fu
n = arange(1,11)
a = (2*n-1)*pi
c = 2*n*pi
b = (a+c)/2

minimas = []
for i in range(len(a)):
    minimas.append(brentGoldenSearch(f,a[i],b[i],c[i],1e-4))
print minimas    
x = brentGoldenSearch(f2,pi,3*pi/2+0.5,pi+pi,1e-5)
print x












    
