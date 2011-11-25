from scipy import *
from numpy import *
from matplotlib.pyplot import *
import scipy.linalg as ln
A = zeros( (8,8) )
for i in range(8):
    for j in range(8):
        A[i][j] = cos(i*j*pi/8)

B = array([[15,3,5,7],
[3, 25, 4, 6],

[5, 4, 10, 5],

[7, 6, 5, 20]])
C = array([[1,1,1,1],
        [1,1,-1.0j,exp(-1.0j*pi/4.0)],
        [1,1.0j,-1,-1.0j],
        [1,exp(1.0j*pi/4.0),1.0j,1]])

Q,R= ln.eig(A)
print Q
print R

print "-------------------------------------------------"
Q,R=ln.eig(B)
#print Q
#print R
print "-----------------------------------------------"
Q,R= ln.eig(C)
#print Q
#print R

R = eye(10,10)
print R.transpose()
