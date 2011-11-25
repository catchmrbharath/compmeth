from numpy import *
from scipy import *
from time import *
from pylab import *
import thread
def functoPlot(printArray):
    for i in range(len(printArray)):
        t = printArray[i]
        figure(1)
        print "reached here"
        plot(t[:,0],t[:,1],'k')
        show()
        sleep(1)
def func(x):
    x = array(x)
    sq = sqrt(x[0]**2 + x[1]**2)
    alpha = 5*(0.1*sq-0.5)
    tran_mat = array([[cos(alpha),sin(alpha)],
                        [-sin(alpha),cos(alpha)]])
    temp = dot(tran_mat,x.transpose())-array([5,5])

    return temp[0]**2 + temp[1]**2
N = 20
x = linspace(-10,10,N)
y = linspace(-10,10,N)
X,Y = meshgrid(x,y)
Z = zeros( (X.shape) )
printArray = []
for i in range(N):
    for j in range(N):
        temp = func([ X[i][j],Y[i][j] ])
        Z[i][j] = temp
a = contour(X,Y,Z)

def getSum(p,psum):
    dim = len(psum)
    for j in range(len(psum)):
        sum = 0
        for i in range(dim+1):
            sum+=p[i][j]
        psum[j] =sum

def amotry(p,y,psum,ihi,fac,func):
    dim = len(psum)
    ptry = linspace(0,0,dim)
    fac1 = (1.0-fac)/dim
    fac2 = fac1-fac
    for j in range(dim):
        ptry[j] = psum[j]*fac1-p[ihi][j]*fac2
    ytry = func(ptry)
    if(ytry<y[ihi]):
        y[ihi] = ytry
        for j in range(dim):
            psum[j]+=(ptry[j]-p[ihi][j])
            p[ihi][j] = double(ptry[j])
    return ytry

def amoeba(p,func,ftol,line):
    N = shape(p)
    dim = N[1]
    mpts =N[0]
    if(mpts!=dim+1):
        return "not working"
    y = linspace(0,0,mpts)
    for j in range(mpts):
        y[j] = func(p[j,:])
    psum = linspace(0,0,dim)
    getSum(p,psum)
    while(1):
        printArray.append(p)
        line.set_xdata(p[:,0])
        line.set_ydata(p[:,1])
        draw()
        ihi = 0
        inhi = 0
        if(y[0]>y[1]):
            ihi = 0
            inhi =1
        else:
            ihi = 1
            inhi = 0

        ilo = 0
        for i in range(mpts):
            if(y[i]<=y[ilo]):ilo = i
            if(y[i]>y[ihi]):
                inhi = ihi
                ihi = i
            elif(y[i]<y[inhi] and i!=ihi):
                inhi = i
        rtol = abs(y[ihi]-y[ilo])
        if(rtol<ftol):
            y[0],y[ilo] = y[ilo],y[0]
            for i in range(dim):
                p[0][i],p[ilo][i]=p[ilo][i],p[0][i]

            break
        ytry = amotry(p,y,psum,ihi,-1.0,func)
        if(ytry<=y[ilo]):
            ytry = amotry(p,y,psum,ihi,2.0,func)
            print "expand"
        elif ytry>=y[inhi]:
            ysave = y[ihi]
            ytry = amotry(p,y,psum,ihi,0.5,func)
            print "contract in one dim"
            if(ytry>=ysave):
                print ilo
                for i in range(mpts):
                    if(i!=ilo):
                        for j in range(dim):
                            p[i][j] = psum[j] = 0.5*(p[i][j]+p[ilo][j])
                        y[i] = func(psum)
                getSum(p,psum)
                print "contract in all dim"



p = array([[8.0,8.0],[8.5,8.5],[8.75,9.0]])
line, = plot(p[:,0],p[:,1])
amoeba(p,func,1e-6,line)
thread.start_new_thread(functoPlot,(printArray,))
show()




