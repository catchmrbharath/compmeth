
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
def integ1_mod(x):
    return sp.jv(3,2.7*x**0.5)*sp.jv(3,2.7*x**0.5)
print romberg(integ1,0,1,EPS =1e-15) 
print romberg(integ1_mod,0,1,EPS = 1e-15)
