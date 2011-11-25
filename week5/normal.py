from scipy import *
from numpy import *
from matplotlib.pyplot import *

def normalpdf(n,m):
    x = zeros((n,m))
    for i in range(n):
        for j in range(m):
            rsq = 2;
            while(rsq>=1.0 or rsq == 0):
                v1 = 2.0*rand()-1
                v2 = 2.0*rand()-1
                rsq = v1*v1+v2*v2
            fac = sqrt(-2.0*log(rsq)/rsq)
            x[i,j]=v1*fac
    return x        

hist(normalpdf(1,100000)[0],100)
show()

