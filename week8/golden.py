from scipy import *
from numpy import *
import scipy.special as sp
from matplotlib.pyplot import *
def sign(a,b):
    if(b>=0):
        return abs(a)
    else:
        return -abs(a)
def dist(x1,x2):
    x1 = array(x1)
    x2 = array(x2)
    if(shape(x1)==shape(x2)):
        return sqrt(sum((x1-x2)**2))
    else:
        print "error"

def bracket(f,ax,bx):
    GOLD = 1.618034
    TINY = 1e-15
    dum =ax
    fu = 0
    fa = f(ax)
    fb = f(bx)
    if(fb>fa):
        ax,bx = bx,ax
        fa,fb=fb,fa
    cx = bx +GOLD*(bx-ax)
    fc = f(cx)
    while(fb>fc):
        r = (bx-ax)*(fb-fc)
        q = (bx-cx)*(fb-fa)
        u = bx-((bx-cx)*q-(bx-ax)*r)/(2.0*sign(max(abs(q-r),TINY),q-r))
        ulim = bx +100.0*(cx-bx)
        if((bx-u)*(u-cx)>0.0):
            fu=f(u)
            if(fu<fc):
                ax = bx
                bx = u
                fa = fb
                fb = fu
                return (ax,bx,cx)
            elif(fu>fb):
                cx = u
                fc = fu
                return (ax,bx,cx)
            u = cx+GOLD*(cx-bx)
            fu = f(u)
        elif ((cx-u)*(u-ulim))>0.0:
            fu = f(u)
            if(fu<fc):
                bx = cx
                cx = u
                u = cx+GOLD*(cx-bx)
                fb = fc
                fc = fu
                fu = f(u)
            elif((u-ulim)*(ulim-cx)>=0):
                u=ulim
                fu = f(u)
            else:
                u = cx+GOLD*(cx-bx)
                fu=f(u)
        ax = bx
        bx = cx
        cx = u
        fa = fb
        fb = fc
        fc = fu
    return (ax,bx,cx)

def brentGoldenSearch(func, ax,bx,cx, tol=1e-4):
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


def linmin(f,p,xi):
    pcom = p[:]
    pcom = array(pcom)
    xicom = xi[:]
    x = 3
    nrfunc = lambda x:  f(pcom+x*xicom)
    ax,bx,cx = bracket(nrfunc,0,1)
    xmin,fmin,it = brentGoldenSearch(nrfunc,ax,bx,cx)
    xi = xi*xmin
    p = p+xi
    return p

def func1(x):
    x = array(x)
    m = array([[ 2.01057304, 1.04351422, 0.11639733, 0.15855415, 0.11737089],
    [ 1.04351422, 1.53763186, 0.93992674, 0.15855415, 0.11737089],
    [ 0.11639733, 0.93992674, 2.26846756, 1.39239668, 0.11737089],
    [ 0.15855415, 0.15855415, 1.39239668, 3.25962827, 1.76056338],
    [ 0.11737089, 0.11737089, 0.11737089, 1.76056338, 2.9342723 ]])
    temp = dot(m,x);
    temp= dot(x.transpose(),temp)
    return temp

def bruteminimize(f,p,tol=1e-4):
    p = array(p)
    N = shape(p)[0]
    xi = linspace(0,0,N)
    cont = True
    funcp = f(p)
    funcl = 1000000
    oldp = array(p[:])
    while True:
       for i in range(N):
           xi = linspace(0.0,0.0,N)
           xi[i] = 1
           oldp = p
           p = linmin(f,oldp,xi)
           funcl = funcp
           funcp = f(p)
           if(abs(funcl-funcp)<tol*abs(funcp)):
               return p
def func2(x):
    x = array(x)
    sq = sqrt(x[0]**2 + x[1]**2)
    alpha = 5*(0.1*sq-0.5)
    tran_mat = array([[cos(alpha),sin(alpha)],
                        [-sin(alpha),cos(alpha)]])
    temp = dot(tran_mat,x.transpose())-array([5,5])

    return temp[0]**2 + temp[1]**2

          
def dfunc2(x):
    x = array(x)
    sq = sqrt(x[0]**2+x[1]**2)
    alpha = 5*(0.1*sq- 0.5)
    tran_mat = array([[cos(alpha),sin(alpha)],
                        [-sin(alpha),cos(alpha)]])
    temp = dot(tran_mat,x.transpose())-array([5,5])
    x1 = x[0]
    y1 = x[1]
    u = temp[0]
    v = temp[1]
    dalphax = 0.5*x1/sq
    dalphay = 0.5*y1/sq
    dux = cos(alpha)-x1*sin(alpha)*dalphax+y1*cos(alpha)*dalphax
    duy = -x1*sin(alpha)*dalphay+sin(alpha)+y1*cos(alpha)*dalphay
    dvx = -sin(alpha)-x1*cos(alpha)*dalphax-y1*sin(alpha)*dalphax
    dvy = -x1*cos(alpha)*dalphay+cos(alpha)-y1*sin(alpha)*dalphay
    return array([2*(u*dux+v*dvx),2*(u*duy+v*dvy)])






    


    


    







