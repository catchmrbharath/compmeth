
from numpy import *
from matplotlib.pyplot import *
import scipy.weave as weave
import scipy.special as  sp
import scipy.integrate as integrate
from week0 import *
def trapz3(funct,a,b,n,s):
    h = b-a
    if(n==1):
        return 0.5*h*(funct(a)+funct(b))
    else:
        it = 1
        for j in range(1,n-1):
            it*=3
        tnm = it
        delta = h/(3.0*tnm)
        x = a+ delta
        sum = 0.0
        for j in range(1,it+1):
            sum += funct(x)
            x += delta
            sum+= funct(x)
            x+=2*delta
        s = (s+(h*sum)/(tnm))/3.0
    return s

def qromb3(func,a,b,EPS = 1.0e-6,full = False):
    JMAX = 20
    JMAXP = JMAX+1
    K = 5

    s = linspace(0.0,0.0,JMAXP)
    h = linspace(0.0,0.0,JMAXP)
    h[0] = 1.0
    y = []
    dy = []
    index = []
    for j in range(JMAX):
       s[j] =trapz3(func,a,b,j+1,s[j])

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
       h[j+1] = h[j]/9.0
     
    print "ERROR"





        


