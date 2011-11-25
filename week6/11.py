from numpy import *
from matplotlib.pyplot import *
import scipy.special as sp

x = linspace(0,13,200)
y = sp.jv(0,x)
plot(x,y,'k')
show()
