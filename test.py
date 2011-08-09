from scipy import *
from matplotlib.pyplot import *
import time
import scipy.weave as weave

a = 0.5
x = arange(0,3,.1)
N =10

def clenc(N,c,x):
    n = len(x)
    y = zeros((N+3,n))
    f = cos(x)
    code = """
    double alpha;
    for(int j=0;j<n;j++){
        alpha = 2.0*f[j];
    for(int k=N; k>0;k--){
        Y2(k,j) = alpha*Y2(k+1,j)- Y2(k+2,j) + c[k];
       }
       f[j] = Y2(2,j)+f[j]*Y2(1,j)+c[0];
      }
      """
    weave.inline(code,["y","c","f","N","n"],compiler = "gcc")
    return (f)
M = 1000
nn = arange(N+2)
c = array(1/(nn*nn+a*a))
fc = clenc(N,c,x)
print fc


