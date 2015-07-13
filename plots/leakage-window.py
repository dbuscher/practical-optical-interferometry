from DftAnalysis import *

x,y1,y2=LeakageSines()
fig,ax=subplots(2,1,sharex=True,sharey=False,figsize=(6*.8,4*.8))
sca(ax[0])
PlotPs(y2)
UnBox()
sca(ax[1])
PlotPs(y2,windowFunction=hanning)
ylim(0,60)
UnBox()
xlabel("frequency index")
ShowOrSave()
