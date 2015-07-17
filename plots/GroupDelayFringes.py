from plotTools import *

def CurvedFringes(nx=100,ny=200,wavelengthRange=(0.8,1.2),numFringes=8.0,delayOffset=20,phaseOffset=0,visibility=1.0):
    wavelength=linspace(wavelengthRange[0],wavelengthRange[1],ny)
    wavenumber=1/wavelength
    delay=linspace(-numFringes/2,numFringes/2,nx)
    phase=2*pi*multiply.outer(wavenumber,delay+delayOffset)+phaseOffset
    fringes=1.0+visibility*sin(phase)
    imshow(fringes,cmap=cm.gray,origin="lower")
    xticks([])
    yticks([])
    xlabel("delay")
    ylabel("wavelength")

def StraightFringes(nx=100,ny=200,wavelengthRange=(0.8,1.2),numFringes=8.0,delayOffset=0,phaseOffset=0,visibility=1.0):
    wavenumber=linspace(1/wavelengthRange[0],1/wavelengthRange[1],ny)
    unperturbedPhase=2*pi*linspace(-numFringes/2,numFringes/2,nx)
    phase=add.outer(2*pi*wavenumber*delayOffset,unperturbedPhase)+phaseOffset
    return 1.0+visibility*sin(phase)
    
def PlotStraightFringes(fringes):
    imshow(fringes,cmap=cm.gray,origin="lower")
    xticks([])
    yticks([])
    xlabel("phase")
    ylabel("frequency")

def PowerSpectrum(fringes):
    window=multiply.outer(hamming(fringes.shape[0]),hamming(fringes.shape[1]))
    return fftshift(abs(fft2(fringes*window))**2)

def PlotPowerSpectrum(fringes):
    pspec=PowerSpectrum(fringes)
    n1,n2=pspec.shape
    imshow(pspec[n1/2-30:n1/2+30,n2/2-30:n2/2+30]**0.3,cmap=cm.gray_r,origin="lower",
           extent=(-30,30,-30,30))
    xticks([-8,0,8])
    yticks([0])
    grid()

