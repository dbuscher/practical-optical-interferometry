from plotTools import *
import temprl
import scipy.signal
import pickle

def ComplexVisibility(phases,nint=1):
    phases=temprl.chop(phases,nint)
    v=np.exp(1j*phases)
    return np.sum(v,axis=-1)/nint

def MeanPhase(phases,nint):
    phases=temprl.chop(phases,nint)
    return np.sum(phases,axis=-1)/nint

def Unwrap(phases):
    diff=zeros_like(phases)
    diff[1:]=phases[1:]-phases[:-1]
    diff=mod(diff+pi,2*pi)-pi
    return add.accumulate(diff)
#phase=pickle.load(open( "ch5/phases.pickle", "rb" ),fix_imports=True )["phase"]
#phase=ascii.read("junk.txt")["phase"]
phase=np.loadtxt(DataFilePath("phase-sequence.txt"))
#for p in phase:
#    print(p)
#    print(float(p))

nint=12
avPhase=MeanPhase(phase,nint)
visPhase=angle(ComplexVisibility(phase,nint))
trackedPhase=Unwrap(visPhase)+avPhase[0]


min=2410*nint
max=min+40*nint
nint=12
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
