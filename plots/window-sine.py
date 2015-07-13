from DftAnalysis import *

x,y1,y2=LeakageSines()
fig,ax=subplots(2,1,sharex=True,sharey=True,figsize=(6,4))
ax[0].plot(x,y2,color="k")
window=hanning(len(y2))
ax[1].plot(x,y2*window,color="k")
ax[1].plot(x,window,color="k",ls="dashed")
ax[1].plot(x,-window,color="k",ls="dashed")
xlabel("pixel")
ylim(-1.1,1.1)
UnBox(ax[0])
UnBox(ax[1])
ShowOrSave()
