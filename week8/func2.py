
from numpy import *
from matplotlib.pyplot import *
import scipy.weave as weave
import scipy.special as  sp
import scipy.integrate as integrate
import scipy.linalg as linal

def func2(x):
    x = array(x)
    sq = sqrt(x[0]**2 + x[1]**2)
    alpha = 5*(0.1*sq-0.5)
    tran_mat = array([[cos(alpha),sin(alpha)],
                        [-sin(alpha),cos(alpha)]])
    temp = dot(tran_mat,x.transpose())-array([5,5])

    return temp[0]**2 + temp[1]**2
N = 20
x = linspace(-10,10,N)
y = linspace(-10,10,N)
X,Y = meshgrid(x,y)
Z = zeros( (X.shape) )
for i in range(N):
    for j in range(N):
        temp = func2([ X[i][j],Y[i][j] ])
        Z[i][j] = temp

contour(X,Y,Z)
show()


