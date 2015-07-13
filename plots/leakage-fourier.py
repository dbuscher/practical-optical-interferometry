from DftAnalysis import *

x,y1,y2=LeakageSines()
fig,ax=subplots(2,1,sharex=True,sharey=True,figsize=(6*.8,4*.8))
sca(ax[0])
PlotPs(y1)
UnBox()
sca(ax[1])
PlotPs(y2)
UnBox()
xlabel("frequency index")
ShowOrSave()
