from scipy import *
from matplotlib.pyplot import *

def ran(rold):
    return (rold*247)%4085

def ran1(rold):
    return (rold*247)%4087

x = linspace(0,0,100000)
y = linspace(0,0,100000)

x1 = linspace(0,0,100000)
y1 = linspace(0,0,100000)
x[0] = 34
y[0] = 230
x1[0] = 29
y1[0] = 34
for i in range(1,len(x)):
    x[i] = ran(x[i-1])
    y[i] = ran(y[i-1])

    x1[i] = ran1(x1[i-1])
    y1[i] = ran1(y1[i-1])
figure(1)
plot(x,y,'ro')
figure(2)
plot(x1,y1,'ro')
show()

