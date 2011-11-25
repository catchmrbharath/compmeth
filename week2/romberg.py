
from numpy import *
import scipy.weave as weave
from trapz import *
from week0 import *
JMAX =20
ORDER = 5
JMAXP = JMAX+1
K=5
def romberg(func, a, b,full = False,EPS = 1e-6):
    s = linspace(0.0,0.0,JMAXP)
    h = linspace(0.0,0.0,JMAXP)
    h[0] = 1.0
    y = []
    dy = []
    index = []
    for j in range(JMAX):
       s[j] = trapz_custom(func,a,b,j+1,s[j])
       if j>K-1:
           p = h[j-K:j+1]
           q = s[j-K:j+1]
           p = p[::-1]
           q = q[::-1]

           ss,dss,x = polint( array(p),array(q),array([0.0]),5)
           print ss,dss
           y.append(ss[0])
           dy.append(dss[0])
           index.append(j)
           if abs(dss)<EPS*abs(ss):
               if full==False:
                   return (ss,j)
               else:
                   return (ss,j,y,dy,index)

            
       s[j+1] = s[j]
       h[j+1] = 0.25*h[j]
     
    print "ERROR"



