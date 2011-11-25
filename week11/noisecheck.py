from numpy import *
from scipy import *
from matplotlib.pyplot import *
from pylab import *
from numpy.fft import *
import scipy.signal as signal
def mfreqz(b,a=1):
    w,h = signal.freqz(b,a)
    h_dB = 20 * log10 (abs(h))
    subplot(211)
    plot(w/max(w),h_dB)
    ylim(-150, 5)
    ylabel('Magnitude (db)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Frequency response')
    subplot(212)
    h_Phase = unwrap(arctan2(imag(h),real(h)))
    plot(w/max(w),h_Phase)
    ylabel('Phase (radians)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Phase response')
    subplots_adjust(hspace=0.5)
    show()
N = 2**16
x = array(randn(N))
y = fftshift(fft(x))
plot(arange(N),abs(y))
b,a = signal.iirdesign(0.12,0.14,1,30,0,ftype ='cheby2')
x2 = signal.lfilter(b,a,x)

y = fftshift(fft(x2))
figure(2)
plot(arange(N),abs(y))
resampx = signal.resample(x2,N/8)
y = fftshift(fft(resampx))
figure(3)

plot(arange(N/8),abs(y))
show()
