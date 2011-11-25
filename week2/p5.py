from numpy import *
import scipy.weave as weave
from trapz import *
from week0 import *
from romberg import *
from trapz import *
import scipy.special as sp
from matplotlib.pyplot import *
def integ1(x) :
    return 2*sp.jv(3,2.7*x)*sp.jv(3,2.7*x)*x

def integ2(x):
    return 2*pow(abs(sp.jv(3,2.7)/sp.kv(3,1.2)),2)*sp.kv(3,1.2*x)*sp.kv(3,1.2*x)*x

def total_integ(x):
    if x<=1 :
       return integ1(x)
     
    else:
        return integ2(x)

romb =  romberg(total_integ,0,15)
print "integration value = %f , no. of function calls = %d" % (romb[0],pow(2,romb[1]))
a =  romberg(integ1,0,1)
b = romberg(integ2,1,15)
ans = a[0]+b[0]
calls = pow(2,a[1]-1)+pow(2,b[1]-1)
print "integration value with splitting = %f no . of function calls = %d "%(ans,calls)

ss,j,y,dy,index = romberg(total_integ,0,15,full = True)
ANS = 0.046038860370705266
print index, dy
y = array(y)
temp = [ANS]*len(index)
temp = array(temp)
dy = array(dy)
index = array(index)
loglog(pow(2,index),abs(dy),'k',color = 'r') 
loglog(pow(2,index),abs(temp-y),'k',color = 'g')
legend(["Estimated error",  "Actual Error"])

ss,j,y,dy,index = romberg(total_integ,0,1,full = True)
ss2,j,y,dy1,index1 = romberg(total_integ,1,15,full = True)
index = array(index)
dy = array(dy)
index1 = array(index1)
dy1 = array(dy1)
print " The integration between 0 and 1 geta an accuracy of 1e-9 with 32 points. SO the scaling is plotted"
figure(3)
title("Error vs no. of function calls after splitting")
loglog(pow(2,index1),abs(dy1),'k',color = 'g') 
show()




