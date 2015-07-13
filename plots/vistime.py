from plotTools import *
from Korff import *

def plotVisTau(min=-1.0,max=2,numPoint=100):
    taulist=logspace(min,max,numPoint,endpoint=True)
    y=array([VsqTau(tau) for tau in taulist])
    figure(figsize=(9*0.75,6*0.75))
    pl.loglog(taulist,y,color="black",lw=1.5,label=r"Numerical result")
    tau0=y[-1]*taulist[-1]
    #print "tau0=",tau0
    pl.loglog(taulist,exp(-(taulist/2.6)**(5./3.)),color="black",
              lw=1.5,ls="dashed",
              label=r"Extended Maréchal")
    taulist=np.array([1.0,10**max])
    pl.loglog(taulist,tau0/taulist,color="black",lw=1.5,ls="dotted",
              label=r"Random walk")
    ylim(0.05,1.1)
    xlim(0.1,50)
    xlabel(r"$\tau/t_0$")
    ylabel(r"$\left\langle|\gamma|^2\right\rangle$")
    legend(loc="lower left")
    ScalarLogAxes()

plotVisTau()
SaveFigure("vistime.pdf")
