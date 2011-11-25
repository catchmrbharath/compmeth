from numpy import *
from matplotlib.pyplot import *
from scipy import *
from scipy.linalg import *
def sign(a,b):
    if(b>=0):
        return abs(a)
    else:
        return -abs(a)
def ratval(x,coeff,mm,kk):
    ans1 = 0.0
    ans2 = 0.0
    power = 1.0
    for i in range(mm+1):
        ans1 += power*coeff[i]
        power*=x
    ans2 = 1.0
    power = 1.0
    for i in range(mm+1,mm+kk+1):
        power*=x
        ans2+=coeff[i]*power
    return ans1/ans2

def svd(u,bb,tol= 1e-8):
    s,v = eigh(dot(u.transpose(),u))
    smin = s.max()*tol
    ii = where(s<smin)
    sinv = 1/s
    sinv[ii]=0
    t = dot(diag(sinv),v.transpose())
    t= dot(v,dot(diag(sinv),v.transpose()))
    
    return dot(t,dot(u.transpose(),bb))
def ratl(func,a,b,mm,kk):
    BIG = 1e30
    NPFAC = 8
    MAXIT = 8
    PIO2 = pi/2.0
    ncof = mm+kk+1
    npt = NPFAC*ncof
    coeff = linspace(0.0,0.0,ncof)
    bb = linspace(0.0,0.0,npt)
    dev = 1000
    ee = linspace(0.0,0.0,npt)
    acoeff = linspace(0.0,0.0,ncof)
    fs = linspace(0.0,0.0,npt)
    u = zeros( (npt,ncof) )
    wt = linspace(0.0,0.0, npt)
    xs = linspace(0.0,0.0,npt)
    for i in range(npt):
        if(i<npt/2.0):
            hth = PIO2*i/(npt-1.0)
            xs[i] = a+(b-a)*(sin(hth)**2)
        else:
            hth = PIO2*(npt-i-1)/(npt-1.0)
            xs[i] = b-(b-a)*(sin(hth)**2)
        fs[i] = func(xs[i])
        wt[i] = 1.0
        ee[i] = 1.0
    e = 0.0
    for it in range(MAXIT):
       for i in range(npt):
            power = wt[i]
            bb[i] = power*(fs[i]+sign(e,ee[i]))
            for j in range(mm+1):
                u[i][j] = power
                power*=xs[i]
            power = -bb[i]    
            for j in range(mm+1,ncof):
                power*=xs[i]
                u[i][j] = power
       coeff = svd(u,bb)
       devmax = 0.0
       sum = 0.0
       for j in range(npt):
           ee[j] = ratval(xs[j],coeff,mm,kk)-fs[j]
           wt[j] = abs(ee[j])
           sum+=wt[j]
           if(wt[j]>devmax): devmax = wt[j]
       e = sum/npt
       if(devmax<dev):
           print dev
           print devmax
           print "reached here"
           acoeff = coeff[:]
           dev = devmax
    return acoeff

def f(x):
    return 1.0/(x**2+2.5)
x = linspace(1,pi,100)
y = f(x)
coeff =ratl(f,1,pi,2,2)
print coeff
y1 = []
for i in range(len(x)):
    y1.append(ratval(x[i],coeff,2,2))
plot(x,y1)
show()



    
