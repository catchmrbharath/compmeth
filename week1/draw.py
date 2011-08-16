n=6 # order of interpolation
xarr=linspace(0,2,11)
yarr=1/(1+xarr*xarr)
t=linspace(0,pi,111)
xx=cos(t)*1.5+1
z=polint(xarr,yarr,xx,n)
yy=z[0];dyy=z[1]
y0=1/(1+xx*xx)
figure(0)
plot(xx,yy,'ro',xx,y0,'k')
title("Interpolation by %dth order polynomial" % n)
figure(1)
semilogy(xx,abs(yy-y0),'ro',xx,abs(dyy),'k')
title("Error in interpolation")
legend(["Actual error","Error Est"])
show()
