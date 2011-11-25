from scipy import *
from matplotlib.pyplot import *
from scipy.linalg import *
import scipy.special as sp
def dataseq(sig,w1,w2,N,k):
  t=(arange(N+0.0)/N)*k
  y=cos(2*pi*(w1*t+w2*t*t+0.1))+sig*randn(N)
  return(y)
def datamatrix(sig,w1,w2,N,k):
  y=dataseq(sig,w1,w2,2*N,2*k)
  A=zeros((N,N))
  for i in range(N):
    A[i,:]=y[i:i+N]
  return(A)
sig=0.01   # noise level (signal is unit amplitude)
w1=0.5      # frequency at t=0
w2=0    # frequency chirp, ie coef of t^{2}
N=100      # number of samples
k=2       # number of wavelengths to sample
n0=4      # number of eigenvalues to keep
A=datamatrix(sig,w1,w2,N,k)
u,s,v=svd(A)
figure(0)
semilogy(s,'ro')
title("svd spectrum")
figure(1)
s[n0:]=0 # zero the noise eigenvalues
B=dot(u,dot(diag(s),v))
figure(1)
plot(B[0,:],'ko',A[0,:],'r+',dataseq(0,w1,w2,N,k),'g')
title("Original signal and reconstruction")
legend(["svd reconstruction","data","signal"])
figure(2)
str=[]
for i in range(n0):
  plot(v[i,:])
  str.append(r"$i=%d$" % i)
title("Profile of eigenvectors")
legend(str)
show()
