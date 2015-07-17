from plotTools import *

def FringePattern(npix,frequency,flux,correlatedFlux,phase,envelopeWidth):
    x=linspace(-npix/2+1,npix/2,npix)
    envelope=exp(-x**2/(2*envelopeWidth**2))
    return flux+correlatedFlux*envelope*cos(2*pi*frequency*x+phase)

def FringePatterns(npix=400):
    return([
    FringePattern(npix,frequency=0.040,flux=1.0,correlatedFlux=0.8,phase=-pi/3,envelopeWidth=51),
    FringePattern(npix,frequency=0.08,flux=0.7,correlatedFlux=0.5,phase=0,envelopeWidth=34),
    FringePattern(npix,frequency=0.12,flux=1.1,correlatedFlux=0.7,phase=pi/2,envelopeWidth=17)])

def PowerSpectrum(v,oversample=2,windowFunction=hamming):
    if windowFunction is not None:
        window=windowFunction(v.shape[-1])
    else:
        window=ones((v.shape[-1],))
    spectrum=abs(fft(v*window,axis=-1,n=v.shape[-1]*oversample))**2
    return spectrum

def Gaussian(x,centre,sigma,amplitude=1):
    return amplitude*exp(-(x-centre)**2/(2*sigma**2))

def f(x): 
    return Gaussian(x,centre=12,sigma=3.4,amplitude=1.5)+Gaussian(x,centre=4,sigma=1.5,amplitude=2.0)-0.04*x

def LeakageSines(npix=200):
    x=arange(npix)
    y1=sin(2*pi/npix*3*x)
    y2=sin(2*pi/npix*3.25*x)
    return x,y1,y2

def PlotPs(y,numFreq=10,width=0.2,windowFunction=None):
    p=sqrt(PowerSpectrum(y,oversample=1,windowFunction=windowFunction))
    xleft=arange(numFreq)-width/2.0
    bar(xleft,p[:numFreq],width,color='0.75')
    xlim(-0.5,numFreq)
    ylim(0,110)
    ylabel("amplitude")


