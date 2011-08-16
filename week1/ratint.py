from scipy import *
import scipy.weave as weave

def ratint(xa,ya,x):
    n = len(xa)
    ans = zeros((2,1))
    c = zeros((n,1),dtype = float)
    d = zeros((n,1), dtype = float) 
    code = """
    #line 120
    #include<math.h>
    #include<stdio.h>
    #define TINY 1.0e-25
    int m,i,ns = 1;
    double w,t,hh,h,dd = 0;
    hh = fabs(x-xa[0]);
    for ( i=0;i<n;i++) {
        h = fabs(x-xa[i]);
        if(h==0.0) {
            ans[0] = ya[i];
            ans[1] = 0.0;
            return 0;
        }
        else if (h<hh) {
            ns = i;
            hh = h;
        }
        c[i] = ya[i];
        d[i] = ya[i] + TINY;
    }
    ans[0] = ya[ns--];
    for ( m=1;m<=n-1;m++) {
        for(i=0;i<n-m;i++) {
            w = c[i+1] - d[i];
            h = xa[i+m] - x;
            t = (xa[i]-x)*d[i]/h;
            
            dd = t - c[i+1];
            if(dd == 0 ) printf("zero error");
            dd = w/dd;
            
            d[i] = c[i+1]*dd;
            c[i] = t*dd;
         }
         ans[1] = (2*ns < (n-m)) ? c[ns+1] : d[ns--];
         ans[0] += ans[1];
         }
         """
    weave.inline(code,["xa","ya","x","c","d","n","ans"], compiler = "gcc")
    return ans

