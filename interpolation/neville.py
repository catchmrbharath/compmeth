import numpy as np
import math
def neville(x,y,testPoints):
    n = len(x)
    points = []
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
    if len(y) <=5 :
        return neville(x,y,testPoints)
    else:
        ans = []
        for k in range(len(testPoints)):
            idx = nearestPoint(x,testPoints[k])


        return ans


x = [1,2,3,4,5,6,7,8,9,10]
fx = np.sin(x)
print fx
testPoints = np.linspace(0,10,100)
print testPoints
ans = neville(x,fx,testPoints)
print ans

       
