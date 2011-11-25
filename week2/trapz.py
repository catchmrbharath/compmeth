from numpy import *
from scipy import *
import scipy.weave as weave
def trapz_custom(funct,a,b,n,s):
    """the function should be called with the previous integration value """ 
    code = """
    #line 7
    double x,tnm,sum,del;
    int it,j;
    py::tuple arg1(1);
    py::tuple arg(1);
    double i1 = (double)a;
    double i2 = (double)b;
    if (n==1) {
        arg[0] = i1;
        arg1[0] = i2;
        
        return_val = 0.5*(i2-i1)*((double)funct.call(arg)+(double)funct.call(arg1));
        }
    else {
        for(it = 1,j=1;j<n-1;j++)
            it<<=1;
        tnm = it;
        del = (double)(i2-i1) /(double) tnm;
        x = i1 + 0.5*del;
        for (sum = 0.0 , j=1;j<=it;j++,x+=del)
        {
            arg[0] = x;
           double  ans = (double)funct.call(arg);
            sum += ans;
        }
            return_val = 0.5*((double)s+ (i2-i1)*sum/tnm);
}
        """
    s = weave.inline(code,["funct","s","a","b","n"],compiler = "gcc")
    return s

def trapzm_custom ( funct, a,b, m):
    """ trapz with (2^m) + 1 points """
    c= 0
    for j in range(1,m+2): 
        c = trapz_custom(funct,a,b,m,c)
    return c



    
