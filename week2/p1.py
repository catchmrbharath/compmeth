from numpy import *
from matplotlib.pyplot import *
import scipy.weave as weave
import scipy.special as  sp
import scipy.integrate as integrate
xa = linspace(0,1,30)
def integ1(x) :
    return 2*sp.jv(3,2.7*x)*sp.jv(3,2.7*x)*x

def integ2(x):
    return 2*pow(abs(sp.jv(3,2.7)/sp.kv(3,1.2)),2)*sp.kv(3,1.2*x)*sp.kv(3,1.2*x)*x

def total_integ(x):
    if x<=1 :
       return integ1(x)
     
    else:
        return integ2(x)

def ansInteg() :
    a = sp.jv(3,2.7)**2 - sp.jv(4,2.7)*sp.jv(2,2.7)
    j3 = sp.jv(3,2.7)
    j2 = sp.jv(2,2.7)
    j4 = sp.jv(4,2.7)
    k2 = sp.kv(2,1.2)
    k3 = sp.kv(3,1.2)
    k4 = sp.kv(4,1.2)
    b = (j3/k3)**2 *(k4*k2 - k3**2)


    return a+ b
ya = map(integ1,xa)
xb = linspace(1,5,20)

yb = map(integ2,xb)
xtest = linspace(0,10,100)
ytest = map(total_integ,xtest)
figure(0)
semilogy(xtest,ytest,'k')
title("The integrand function")
yans = integrate.quad(total_integ,0,50)
print yans
yint = integrate.quad(total_integ,0,50,full_output=1)
print "No. of function calls by quad = %d" %yint[2]['neval']
split1 = integrate.quad(total_integ,0,1,full_output = 1)
split2 = integrate.quad(total_integ,1,50,full_output = 1)
print "Number of function calls after splitting quad = %d "%(split1[2]['neval'] + split2[2]['neval'])

temp = []

for i in range(10,500):
    x = linspace(0,10,i)
    y = map(total_integ,x)
    temp.append( abs(yint[0]-integrate.trapz(y,x)))
figure(2)    
loglog((range(10,500)),temp,'k')
title("Error vs number of terms( trapezoid")
temp2 = []
temp = []
x1 = []
x2 = []
for i in range(10,500):
    x = linspace(0,10,i)
    y = map(total_integ,x)
    if 1.0 in x:
        temp.append( abs(yint[0]-integrate.trapz(y,x)))
        x1.append(i)
    else:
        x2.append(i)
        temp2.append( abs(yint[0]-integrate.trapz(y,x)))
figure(3)
loglog(x1,temp,'k',color = 'b')
loglog(x2,temp2,'k',color = 'r')
legend(["1.0 is a data point","1.0 is not a data point"])
show()
