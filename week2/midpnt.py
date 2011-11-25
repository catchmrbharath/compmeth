
from numpy import *
import scipy.weave as weave

def midpnt1(funct,x1,x2,n,s):
    code = """
        #line 8
        double x,tnm,sum,del ,ddel;
        int it,j;
        double a = (double) x1;
        double b = (double) x2;
        py::tuple arg(1);
        if(n==1){
            arg[0] = 0.5*(a+b);
            return_val = (b-a)*(double)funct.call(arg);
            }
        else {
            for(it = 1,j=1;j<n-1;j++) it*=3;
            tnm = it;
            del = (b-a)/(3.0*tnm);
            ddel = 2*del;
            x = a + 0.5*del;
            sum = 0.0;
                for (j =1 ;j<=it;j++){
                    arg[0] = x;
                    sum = sum + (double)funct.call(arg);
                    x +=ddel;
                    arg[0] = x;
                    sum = sum + (double)funct.call(arg);
                    x+=del;
                    }
          return_val = (double)((double)s + (b-a)*sum/tnm)/3.0;
          }
          """
    s = weave.inline(code,["funct","s","x1","x2","n"],compiler = "gcc")
    return s

def midpntm ( funct, a,b, m):
    """ trapz with (2^m) + 1 points """
    c= 0
    for j in range(1,m+2): 
        print j
        c = midpnt1(funct,a,b,j,c)

    return c

