from DftAnalysis import *

x,y1,y2=LeakageSines()
fig,ax=subplots(2,1,sharex=True,sharey=True,figsize=(6,4))
ax[0].plot(x,y1,color="k")
ax[1].plot(x,y2,color="k")
xlabel("pixel")
ylim(-1.1,1.1)
UnBox(ax[0])
UnBox(ax[1])
ShowOrSave()
