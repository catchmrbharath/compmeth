from scipy import *
from numpy import *
import string
from matplotlib.pyplot import *
import numpy.fft as fft
f = open('tek00013.dat','r')
x = []
y = []
for lines in f:
    temp = lines.rsplit()
    x.append(float(temp[0]))
    y.append(float(temp[1]))

y = array(y)
fourier = fft.fft(y,2**16)
tempfourier1 = fourier[0:2**15]
tempfourier2 = fourier[2**15:2**16]
#fourier = append(tempfourier2,tempfourier1)
fourier2 = fft.fftshift(fourier)
freq = linspace(-25*1e6,25*1e6,2**16)
plot(freq,abs(fourier2),'k')

#windowing the data
def fourier(y,N,f):
    print N
    fourier = fft.fftshift(fft.fft(y,2**N))
    
    freq = linspace(-f,f,2**N)
    return fourier,freq

F = 25*1e6
for i in range(6,12):
    n = 2**i
    tempy = y[25000-n/2:25000+n/2]
    four,freq = fourier(tempy,i,F)
    #plot(freq,abs(four))
#better window
a = y[25000-542/2:25000+542/2]
freq = linspace(-F,F,542)
four = fft.fftshift(fft.fft(a))
#figure(2)
#plot(freq,four)

