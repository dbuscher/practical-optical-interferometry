from plotTools import *
from Korff import *

ScalarAxes=ScalarLogAxes

def SnrTau(min=-1.0,max=2,numPoint=100):
    taulist=logspace(min,max,numPoint,endpoint=True)
    y=array([VsqTau(tau) for tau in taulist])
    return taulist,y

taulist,y=SnrTau()
figure(figsize=(10,5))
ax=subplot(1,2,1)
pl.loglog(taulist,y*sqrt(taulist),color="k",label="Photon-noise-limited")
xlabel(r"$\tau_{\rm exp}/t_0$")
ylabel(r"relative SNR")
ScalarAxes()

ax=subplot(1,2,2)
pl.loglog(taulist,y*taulist**1.5,color="k",label="Read-noise-limited")
ylim(0.05,20)
xlabel(r"$\tau_{\rm exp}/t_0$")
ScalarAxes()

ShowOrSave()
