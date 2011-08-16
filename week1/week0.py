from scipy import *
from matplotlib.pyplot import *
import scipy.weave as weave
def polint(xarr,yarr,xx,n):
  M=len(xarr);N=len(xx)
  c=zeros((n+1,1));d=zeros((n+1,1))
  yy=zeros(xx.shape);dyy=zeros(xx.shape)
  code="""
  #include<math.h>
  int i,j,n1,m,ns,ns0;
  double den,dift,ho,hp,w;
  double *xa,*ya,*x,*y,*dy; // window to use by polint
  c[0]=d[0]=0.0;
  xa=xarr;ya=yarr; // initialize pointers
  for(j=0,n1=0;j<N;j++){ // loop over xarr points
    x=&xx[j];y=&yy[j];dy=&dyy[j];
    for(i=n1,ns=M-1;i<M;i++){ // loop over x points
      if(*x<=xarr[i]){ // found crossover
        ns=i;
        break;
      }
    } // i loop
    if( i==n1 ){
      for(ns=n/2;i>=0;i--){ // loop over x points
        if(*x>xarr[i]){ // found crossover
          ns=i;
          break;
        }
      } // i loop
    }
    n1=ns-n/2;
    n1=(n1<0?0:n1); // eliminate -ve n1
    n1=(n1+n>=M?M-n-1:n1); // eliminate +v overflow
    xa=&xarr[n1];ya=&yarr[n1];
    ns-=n1;ns=(ns<n/2?n/2:ns);
    ns0=ns;
    // from here it is basically the NR code
    for(i=0;i<=n;i++){ // initialize c and d
      c[i]=ya[i];
      d[i]=ya[i];
    }
    *y=ya[ns--];
    for(m=1;m<=n;m++){
      for(i=0;i<=n-m;i++){
        ho=xa[i]-*x;
        hp=xa[i+m]-*x;
        w=c[i+1]-d[i];
        if((den=(ho-hp))==0.0)
          exit(1);
        den=w/den;
        d[i]=hp*den;
        c[i]=ho*den;
      } // i loop
      *y+=(*dy=(2*ns<(n-m)?c[ns+1]:d[ns--]));
    } // m loop
  } // j loop
  """
  weave.inline(code,   ["xarr","yarr","M","xx","yy","dyy","N","c","d","n"],compiler="gcc")
  return([yy,dyy,xx])

