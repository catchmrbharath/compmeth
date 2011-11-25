from numpy import *
from matplotlib.pyplot import *
from scipy import *

def radius(x):
    n = shape(x)
    radius=x[0,:]*x[0,:]
    for i in range(1,n[0]):
        radius+=(x[i,:]*x[i,:])
    return radius
def idealRadius(x):
    return pi**(x/2)/factorial(x/2)
colors = ["r","g","b","y","c"]
label = []
for i in range(2,11,2):
    y = []
    trial = arange(1000,100000,1000)
    for j in trial:
        N = j
        x = rand(i,N)
        x = 2*x-1
        a = where(radius(x)<1)
        y.append( (shape(a)[1]/double(N))*(2**i))
    semilogy(trial,y,'or',color = colors[i/2-1])
    semilogy(trial,[idealRadius(i)]*shape(trial)[0],'k')
    label.append("$ n= $"+str(i))
    label.append(" ")
legend(label)
show()
