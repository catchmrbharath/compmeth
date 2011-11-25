from numpy import *

import string
from matplotlib.pyplot import *
import numpy.fft as fft
f = open('tek00013.dat','r')
x = []
y = []
for lines in f:
    temp = lines.rsplit()
    x.append(float(temp[0]))
    y.append(float(temp[1]))

y = array(y)

N = 1000
count = 0
freq = []
for i in range(50000/N):
    count = 0
    for j in range(N):
        if(y[i*N+j]<=0 and y[i*N+j+1]>0):
            count+=1
    freq.append((float(count)/N)*25*1e6)
plot(arange(50000/N),freq,'k')
show()



