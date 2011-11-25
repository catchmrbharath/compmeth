
from scipy import *
from numpy import *
from matplotlib.pyplot import *
import scipy.linalg as ln
A = zeros( (8,8) )
for i in range(8):
    for j in range(8):
        A[i][j] = cos(i*j*pi/8)

B = array([[15,-3,-5,-7],
[-3, 25, -4, -6],

[-5, -4, 10, -5],

[-7, -6, -5, 20]])
C = array([[1,1,1,1],
        [1,1,-1.0j,exp(-1.0j*pi/4.0)],
        [1,1.0j,-1,-1.0j],
        [1,exp(1.0j*pi/4.0),1.0j,1]])

def householder(a): 
    n = len(a)
    for k in range(n-2):
        u = a[k+1:n,k]
        uMag = sqrt(dot(u,u))
        if u[0] < 0.0: uMag = -uMag
        u[0] = u[0] + uMag
        h = dot(u,u)/2.0
        v = dot(a[k+1:n,k+1:n],u)/h
        g = dot(u,v)/(2.0*h)
        v = v - g*u
        a[k+1:n,k+1:n] = a[k+1:n,k+1:n] - outer(v,u) \
                         - outer(u,v)
        a[k,k+1] = -uMag
    return diagonal(a),diagonal(a,1)

def eigenm(B):
    c,d= householder(B)
    a = diag(c,0)+diag(d,1)+diag(d,-1)
    q,r = ln.qr(a)
    for i in range(100):
        q,r = ln.qr(a);
        a = dot(r,q);
    return sort(diag(a,0))

print eigenm(A)
