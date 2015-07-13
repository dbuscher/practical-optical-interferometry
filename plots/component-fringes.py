from DftAnalysis import *

fig,ax=subplots(3,1,sharex=True,sharey=True,figsize=(6,4))
for i,fringe in enumerate(FringePatterns()):
    sca(ax[i])
    plot(fringe,color="k")
    ylabel("intensity")
    ylim(0,1.9)
    UnBox()
xlabel("pixel")
ShowOrSave()

