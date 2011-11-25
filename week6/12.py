from numpy import *
from matplotlib.pyplot import *
import scipy.special as sp
def brentBisection(func,x1,x2,tol = 1e-6):
    MAXITR = 100
    EPS = 1e-8
    count = 0
    a = x1
    b = x2
    c = x2
    e = 0.0
    d = 0.0
    s = 0.0 
    p = 0.0
    q = 0.0 
    fa = func(x1)
    fb = func(x2)
    count+=2
    if((fa>0 and fb>0) or (fa<0 and fb<0)):
        print "Error roots have to be bracketed"
        return None
    fc = fb
    for itr in xrange(1,MAXITR):
        if((fb>0 and fc>0 ) or (fb<0 and fc<0)):
            c = a
            fc = fa
            e = b-a
            d = b-a
        if (abs(fc)<abs(fb)):
            a =b 
            b = c
            c = a
            fa = fb
            fb = fc
            fc = fa
        tol1 = 2*EPS*abs(b)+0.5*tol
        xm = 0.5*(c-b)
        if(abs(xm)<=tol1 or fb == 0.0 ): return b,count
        if(abs(e)>=tol1 and abs(fa)>abs(fb)):
            s = fb/fa
            if a==c:
                p = 2.0*xm*s
                q = 1.0 -s
            else:
                q = fa/fc
                r = fb/fc
                p = s*(2.0*xm*q*(q-r)-(b-a)*(r-1.0))
                q = (q-1.0)*(r-1.0)*(s-1.0)
            if p>0.0: q = -q
            p = abs(p)
            min1 = 3.0*xm*q - abs(tol1*q)
            min2 = abs(e*q)
            temp = 0.0
            if min1<min2: temp = min1
            else: temp = min2

            if(2.0*p < temp):
                e = d
                d = p/q
            else:
                d = xm
                e =d 
        else:
            d = xm
            e =d 
        a = b
        fa = fb
        if(abs(d)>tol1):
           b+=d
        else:
           if(xm>0): b+=abs(tol1)
           else: b-=abs(tol1)
        fb = func(b)
        count+=1
def f(x):
    return sp.jv(0,x)
a = []
pts = arange(11)*pi
print pts
for i in range(1,len(pts)):
   a.append(brentBisection(f,pts[i-1],pts[i]))
print a
print 
