from plotTools import *

def chop(samples,maxLag):
    """Chop a 1-d array into a 2-d array of slices of length maxLag.  The
    length of samples does not have to be a multiple of maxlag - the remainder
    is discarded"""
    maxSamp=len(samples)
    numWindow=int(maxSamp/maxLag)
    numSamp=numWindow*maxLag
    return samples[:numSamp].reshape(numWindow,maxLag)

def ComplexVisibility(phases,nint=1):
    """Return the complex visibility for a coherent integration of
    nint samples of the phase"""
    phases=chop(phases,nint)
    v=np.exp(1j*phases)
    return np.sum(v,axis=-1)/nint

def MeanPhase(phases,nint):
    """Boxcar-average a phase sequence"""
    phases=chop(phases,nint)
    return np.sum(phases,axis=-1)/nint

def Unwrap(phases):
    """Unwrap a sequence of phases to track phase excursions of more than 2pi"""
    diff=zeros_like(phases)
    diff[1:]=phases[1:]-phases[:-1]
    diff=mod(diff+pi,2*pi)-pi
    return add.accumulate(diff)

#Read in simulated time sequence of data
phase=np.loadtxt(DataFilePath("phase-sequence.txt"))
nint=12
avPhase=MeanPhase(phase,nint)
visPhase=angle(ComplexVisibility(phase,nint))
trackedPhase=Unwrap(visPhase)+avPhase[0]

# Select a suitable subset of the data to plot
min=2410*nint
max=min+40*nint

t0=12.
avPhase=MeanPhase(phase[min:max],nint)
trackedPhase=Unwrap(angle(ComplexVisibility(phase[min:max],nint)))+avPhase[0]
diff=trackedPhase-avPhase
plot(arange(max-min)/t0,phase[min:max]/(2*pi),color="0.5",label="fringe phase")
plot(arange(len(trackedPhase))*nint/t0,trackedPhase/(2*pi),"o-",color="0.0",label="tracked phase")
xlabel("Time/$t_0$")
ylabel("Phase (cycles)")
legend(loc="lower right")
ShowOrSave()
