from scipy import *
from matplotlib.pyplot import *
from scipy.linalg import *
import scipy.special as sp
def q1f(x,sig):
  return exp(x)+sig*randn(len(x),1)


x=arange(0.1,2.05,0.1).reshape((20,1))
b=q1f(x,0)
M=hstack([ones(shape(x)),x,x*x,x**3,x**4,x**5,x**6])
figure(0)
plot(x,M,x,b)
legend(["x^0","x^1","x^2","x^3","x^4",
  "x^5","x^6","b"])
title("Plot of the columns of M and of b")
A=dot(M.transpose(),M)
print eigh(A)[0]
#figure(1)
#contour(20*log10(A))
c=dot(inv(A),dot(M.transpose(),b))
figure(2)
semilogy(eigh(A)[0])
title("Semilog plot of eigen values of A")
def pinv(M,tol):
  A=dot(M.transpose(),M)
  s,v=eigh(A)
  smin=s.max()*tol
  ii=where(s<smin)
  sinv=1/s # assumes non singular
  sinv[ii]=0 # zeros the "bad singular values"
  return dot(v,dot(diag(sinv),v.transpose()))
c0=1/sp.gamma(arange(1,8)).reshape(7,1)
Tols=logspace(-12,-2,6)
err=zeros(6)
figure(3)
s=[]
for i in range(6):
  c=dot(pinv(M,Tols[i]),dot(M.transpose(),b))
  err[i]=(abs(c-c0)).max()
  plot(x,dot(M,c)/b-1)
  s.append("tol=%.1e" % Tols[i])
  print "Tol = %.4e, max Err=%5f" % (Tols[i],err[i])
  for k in range(len(c)):
    print "%5f\t%5f\t%5f" % (c[k],c0[k],c[k]-c0[k])
legend(s)
figure(4)
loglog(Tols,err,'b',Tols,err,'bo')
title("error in coefficients vs tolerance");
show()
