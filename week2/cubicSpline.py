import scipy.weave as weave
from numpy import *
from scipy import *
def cubicSpline(x,y,splineType,*params):
    n = len(x)
    y2 = zeros((n+1,1))
    u = zeros((n+1,1))
    un = 0.0
    qn = 0.0
    if splineType == "clamped":
        ydiffPoint1 = params[0]
        ydiffPointn = params[1]
        y2[0] = -0.5
        u[0]=(3.0/(x[1]-x[0]))*((y[1]-y[0])/(x[1]-x[0])-ydiffPoint1)
    	qn=0.5
        un=(3.0/(x[n-1]-x[n-2]))*(ydiffPointn-(y[n-1]-y[n-2])/(x[n-1]-x[n-2]))
    if splineType == "natural":
        y2[0] = 0.0
        u[0] = 0.0
        qn = 0.0
        un = 0.0 
    if splineType == "notaknot":
        y2[0] = 1
        u[0] = 0
        qn = -1
        un = 0

    code = """
    #line 29
    #include<math.h>
    int i,k;
    double p,sig;
	for (i=1;i<n-1;i++) {
		sig=(x[i]-x[i-1])/(x[i+1]-x[i-1]);
		p=sig*y2[i-1]+2.0;
		y2[i]=(sig-1.0)/p;
		u[i]=(y[i+1]-y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1]);
		u[i]=(6.0*u[i]/(x[i+1]-x[i-1])-sig*u[i-1])/p;
	}
	y2[n-1]=((double)un-(double)qn*u[n-2])/((double)qn*y2[n-2]+1.0);
	for (k=n-2;k>=0;k--)
		y2[k]=y2[k]*y2[k+1]+u[k];
"""

    weave.inline(code,["x","y","qn","un","n","y2","u"],compiler = "gcc")
    return y2

def splint(xa,ya,y2a,x):
    n = len(xa)
    y = 0.0
    code = """
    #line 52
    #include<stdio.h>
    int low = 0;
    int high = n-1;
    int average = 0;
    while(high-low > 1) {
        average = (int)(high+low)>>1;
        if(xa[average]>(double)x) high = average;
        else low = average;
        }
        double h = xa[high] - xa[low];
        double a = (xa[high] - (double)x)/h;
        double b = ((double)x - xa[low])/h;
        y = a*ya[low] + b*ya[high] + ((a*a*a-a)*y2a[low] + (b*b*b - b)*y2a[high])*(h*h)/6.0;
        return_val = y;
    """
    y = weave.inline(code, ["xa","ya","y2a","x","y","n"],compiler = "gcc")
    return y

def splintList(xa,ya,y2a,x):
    temp = []
    for i in range(len(x)):
        temp.append(splint(xa,ya,y2a,x[i]))
    return temp





