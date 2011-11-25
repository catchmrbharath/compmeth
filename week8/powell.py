
from scipy import *
from numpy import *
import scipy.special as sp
from golden import *
def sqr(x):
    return x*x
def powell(f,p,xi,tol=1e-6):
    COUNTMAX = 200
    pt = p[:]
    fret = f(p)
    ptt=p[:]
    xit = p[:]
    count = 0
    fp = 0.0
    n = shape(p)[0]
    while(True):
        count+=1;
        fp = fret
        ibig = 0.0
        delt = 0.0
        for i in range(n):
            xit = xi[:,i]
            fptt = fret
            p = linmin(f,p,xit)
            fret = f(p)
            if(abs(fptt-fret)>delt):
                delt = abs(fptt-fret)
                ibig = i
        if(2.0*abs(fp-fret)<=tol*(abs(fp)+abs(fret))):
            return p
        if(count>COUNTMAX):
            print error("max iterations exceeded")
        ptt = 2*p[:]-pt[:]
        xit = p[:] - pt[:]
        pt = p[:]
        fptt = f(ptt)
        if(fptt<fp):
            t = 2.0*(fp-2.0*fret+fptt)*sqr(fp-fret-delt)-delt*sqr(fp-fptt)
            if(t<0.0):
                p = linmin(f,p,xit)
                fret = f(p)
                xi[:,ibig] = xi[:,n-1]
                xi[:,n-1] = xit
def conj(f,p,df,tol=1e-5):
    n = shape(p)[0]
    COUNTMAX =200
    EPS = 1e-10
    xi = df(p)
    g = -xi[:]
    h = g[:]
    xi = h[:]
    fret = f(p)
    fp = fret
    for i in range(COUNTMAX):
        p = linmin(f,p,xi)
        fret = f(p)
        if(2.0*abs(fret-fp)<=tol*(abs(fret)+abs(fp)+EPS)):
                return p
        fp = f(p)
        xi = df(p)
        dgg= gg =0.0
        for j in range(n):
            gg+=g[j]*g[j]
            dgg+=(xi[j]+g[j])*xi[j]
        if(gg==0):
            return p
        gam = dgg/gg
        for j in range(n):
            g[j] = -xi[j]
            h[j] = g[j] + gam*h[j]
            xi[j] = h[j]







    

N = 2
xi = zeros( (N,N) )
p = array([5,5])
for i in range(N):
    xi[i][i] = 1
p = conj(func2,p,dfunc2)
print p


        

        
        


