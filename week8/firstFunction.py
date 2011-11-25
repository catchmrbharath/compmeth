
from numpy import *
from matplotlib.pyplot import *
import scipy.weave as weave
import scipy.special as  sp
import scipy.integrate as integrate
import scipy.linalg as linal

def func1(x):
    x = array(x)
    m = array([[ 2.01057304, 1.04351422, 0.11639733, 0.15855415, 0.11737089],
    [ 1.04351422, 1.53763186, 0.93992674, 0.15855415, 0.11737089],
    [ 0.11639733, 0.93992674, 2.26846756, 1.39239668, 0.11737089],
    [ 0.15855415, 0.15855415, 1.39239668, 3.25962827, 1.76056338],
    [ 0.11737089, 0.11737089, 0.11737089, 1.76056338, 2.9342723 ]])
    w,v= linal.eigh(m)
    temp = dot(m,x);
    return  dot(x.transpose(),temp)


N = 20

valueArr = zeros ((20,5))
x = linspace(-5,5,20)
y = linspace(-5,5,20)
X,Y = meshgrid(x,y)
Z = zeros( ( X.shape))
for i in range(20):
    for j in range(20):
        temp = func1([X[i][j],Y[i][j],2,2,2])
        Z[i][j] = temp
contour(X,Y,Z)

startdict = {'x':10,'y':10,'z':10,'v':10,'w':10}

def minimize(func1,present, direct,startEPS = 1e-3):
    present = array(present)
    direct = array(direct)
    startVector = present
    startValue = func1(present)
    endValue = func1(present+startEPS*direct)
    endVector = present + startEPS*direct
    if(startValue<endValue):
        direct = -1*direct
        endValue = func1(present+startEPS*direct)
        endVector = present+startEPS*direct

    print startValue, endValue
    count = 1
    while(startValue>endValue):
        startValue = endValue
        count*=2
        startVector = endVector
        endValue = func1(present+startEPS*count*direct)
        endVector = present + startEPS*count*direct
    print startVector, endVector

minimize(func1,[10,10,10,10,10],[1.0,0,0,0,0])

def golden_search(func1,x1,x2,x3,direct,EPS=1e-3):
    double phi = (1+ Math.sqrt(5)) /2.0
    double resphi = 2 - phi




