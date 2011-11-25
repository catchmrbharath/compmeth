import scipy.weave as weave
from numpy import *
from scipy import *
from cubicSpline import *
def splineInteg(x,y,integType):
    y2a = cubicSpline(x,y,integType)
    n = len(x)
    sum = 0
    for i in range(n-1):
        h = x[i+1]-x[i]
        sum = sum + h*(y[i+1]+y[i])/2.0
        sum = sum - h*h*h*(y2a[i+1]+y2a[i])/24.0
    return sum

