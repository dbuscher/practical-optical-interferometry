from plotTools import *

def snr(atmsnr,x):
    return 1/sqrt(1/atmsnr**2+2/x**2+1/x**4)

x=logspace(-2,4,100)
y=snr(100.0,x)
ylim(2e-4,4e2)
loglog(x,y,color="k")
xlabel(r"$SNR_{\hat F}$")
ylabel(r"$SNR_{\hat P}$")
SaveFigure("powerspectrum-scaling.pdf")
