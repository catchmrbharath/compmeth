from scipy import *
from matplotlib.pyplot import *
import scipy.weave as weave
from week0 import polint
xarr = linspace(0,1,5)
yarr = sin(6*xarr*xarr)
xx = linspace(-0.5,1.5,200)
n = 4
z = polint(xarr,yarr,xx,n)
yacc = sin(6*xx*xx)
yy = z[0]
dy = z[1]
figure(0)
plot(xx,yy,'ro',xx,yacc,'k')
title("Interpolation by %dth order polynomial" % n )
figure(1)
semilogy(xx,abs(yacc-yy),'ro',xx,dy,'k')
title("Error plot")
legend(["Actual Error","estimated error"])
show()

