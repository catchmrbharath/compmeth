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


