from numpy import *
import scipy.weave as weave
from trapz import *
from week0 import *
from romberg import *
from trapz import *
import scipy.special as sp
from romb3 import *
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



ss,j,y,dy,index= romberg(total_integ,0,15,full = True)
ANS = 0.046038860370705266
y = array(y)
temp = [ANS]*len(index)
temp = array(temp)
dy = array(dy)
index = array(index)
loglog(pow(2,index),abs(dy),'k',color = 'r') 

ss,j,y,dy,index= qromb3(total_integ,0,15,full = True)
y = array(y)

temp = [ANS]*len(index)
temp = array(temp)
dy = array(dy)
index = array(index)
loglog(pow(3,index),abs(dy),'k',color = 'g') 
legend(["standard romberg", "3 romberg"])
show()
