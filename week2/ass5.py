
from numpy import *
from matplotlib.pyplot import *
import scipy.weave as weave
import scipy.special as  sp
import scipy.integrate as integrate
from givenFunction import *


yint = integrate.romberg(total_integ,0,10,show = True,tol = 1e-3)
print yint
