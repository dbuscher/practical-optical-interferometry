from plotTools import *
import scipy.signal

def RcFilter(samples,tau):
    e=exp(-1.0/tau)
    return scipy.signal.lfilter([1-e],[1,-e],samples,axis=0)

def chop(samples,blockSize):
    """Chop first dimension of array into a 2-d array of blocks of length blockSize.  The
    original dimension does not have to be a multiple of blockSize - the remainder
    is discarded. Will return an error for arrays which cannot be reshaped in this
    way without copying"""
    maxSamp=samples.shape[0]
    numBlock=maxSamp//blockSize
    numSamp=numBlock*blockSize
    self=samples[:numSamp].view()
    self.shape=(numBlock,blockSize)+samples.shape[1:]
    return self

def BlockAverage(samples,blockSize):
    return sum(chop(samples,blockSize),axis=1)/float(blockSize)

def DispersedFringes(delay,wavenumberRange,numChan):
    wavenumber=linspace(wavenumberRange[0],wavenumberRange[1],numChan)
    fringePhase=multiply.outer(delay,wavenumber)
    v=exp(1j*fringePhase)
    return v
    
def PowerSpectrum1d(v,oversample=2):
    window=hamming(v.shape[-1])
    return fftshift(abs(fft(v*window,axis=-1,n=v.shape[-1]*oversample))**2,axes=(-1,))

def ComplexNoise(shape,sigma=1.0):
    r=np.random.normal(size=shape+(2,),scale=sigma/sqrt(2))
    return r[...,0]+1j*r[...,1]

def GroupDelaySimulation(phase,wavenumberRange,numChan,numCoherent,numIncoherent,SNR):
    coherentVisibilities=BlockAverage(DispersedFringes(phase,wavenumberRange,numChan),numCoherent)
    coherentVisibilities+=ComplexNoise(coherentVisibilities.shape,sigma=sqrt(numChan)/SNR)
    delaySpectrum=RcFilter(PowerSpectrum1d(coherentVisibilities),numIncoherent)
    return delaySpectrum

def PlotGroupDelaySimulation(phase,t0=12,numChan=100,wavenumberRange=(0.8,1.2),
                             numCoherent=16,numIncoherent=25,incoherentOverSampling=2,SNR=1,numSkip=20):
    figure(figsize=(5,5))
    sampling=numIncoherent/incoherentOverSampling
    spectrum=GroupDelaySimulation(phase,wavenumberRange,numChan,numCoherent,numIncoherent,SNR)[::sampling]
    dmax=numChan/(2*(wavenumberRange[1]-wavenumberRange[0]))
    imshow(transpose(spectrum[numSkip:]),cmap=cm.gray_r,origin="lower",aspect="auto",
           extent=(0,len(phase)/t0,-dmax,dmax))
    xlabel("time/$t_0$")
    ylabel("delay (wavelengths)")
