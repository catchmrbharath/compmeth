import numpy as np
from numpy import *
import math
def neville(x,y,testPoints):
    n = len(x)
    points = []
    print "point = " 
    print testPoints
    for k in range(len(testPoints)):
        fx = y[:]    
        for i in range(2,n):
            for j in range(n-i+1):
                temp = ((testPoints[k] - x[j+i-1])*fx[j] + (x[j]-testPoints[k])*fx[j+1])/(x[j]-x[j+i-1])
                fx[j] = temp
        points.append(fx[0])
    return points

def nearestPoint(x,testPoint):
    return np.abs(x-testPoint).argmin()

def nevilleLargeNumber(x,y,testPoints):
    if len(y)<5 :
        return neville(x,y,testPoints)
    else:
        ans = []
        for k in range(len(testPoints)):
            idx = nearestPoint(x,testPoints[k])
            print idx
            if 1<idx<len(x)-2:
                temp1 = (neville(x[idx-2:idx+2],y[idx-2:idx+2],list(testPoints[k])))
            elif idx<=1:
                temp1 = (neville(x[0:4],y[0:4],array((testPoints[k]))))
            else:
                temp1 = (neville(x[-4:],y[-4:],array(list(testPoints[k]))))
            print temp1
    return ans


x = array([1,2,3,4,5,6,7,8,9,10])
fx = np.sin(x)
print fx
testPoints = array([1,2,3,4,5,6,7,8,9,10])
print testPoints
ans = nevilleLargeNumber(x,fx,testPoints)
print ans

       
