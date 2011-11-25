from numpy import *
import scipy.weave as weave
from trapz import *
from week0 import *
from romberg import *
from trapz import *
import scipy.special as sp
from cubicSpline import *
from splineInteg import *
import scipy.integrate as integ
def integ1(x) :
    return 2*sp.jv(3,2.7*x)*sp.jv(3,2.7*x)*x

def integ2(x):
    return 2*pow(abs(sp.jv(3,2.7)/sp.kv(3,1.2)),2)*sp.kv(3,1.2*x)*sp.kv(3,1.2*x)*x

def total_integ(x):
    if x<=1 :
       return integ1(x)

    else:
        return integ2(x)
x = linspace(0,15,3000)
y = map(total_integ,x)
print "The test answer with 3000 points is %f" %splineInteg(array(x),array(y),"knotanot")

ANS = 0.046038860370705266
error = []
for i in range(3,15):
    x = linspace(0,15,2**i)
    y = map(total_integ,x)
    ans = splineInteg(array(x),array(y),"knotanot")
    error.append(ANS - ans)
figure(1)
loglog(pow(2,array(range(3,15))),abs(array(error)),'k')
title("error vs no. of function calls")

x = linspace(0,10,100)
y = map(total_integ,x)
xtest = linspace(0,10,500)
x = array(x)
y = array(y)
xtest = array(xtest)
y2a =cubicSpline(x,y,"knotanot")
ytest = splintList(x,y,y2a,xtest)
figure(2)
title("spline interpolated function")
semilogy(xtest,ytest,'k')
x1 = linspace(0,1,64)
y1  = map(total_integ,x1)
tans = splineInteg(array(x1),array(y1),"knotanot")
print tans
error = []
for i in range(3,15):
    x = linspace(1,15,2**i)
    y = map(total_integ,x)
    ans = splineInteg(array(x),array(y),"knotanot")
    error.append(ANS - ans[0]-tans)
figure(1)
print error
print tans
print  pow(2,array(range(3,15)))
print array([32]*len(range(3,15)))

xaxis = pow(2,array(range(3,15)))+([64]*len(range(3,15)))
loglog(xaxis,abs(array(error)),'k',color = 'g')
legend(["without splitting", "after splitting"])
show()



