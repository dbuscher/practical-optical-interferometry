from plotTools import *

fig, ax = plt.subplots(2, 2, sharex='col',figsize=(0.6*12,0.6*5))
for row,width in ((0,0.5),(1,1.0)):
    sca(ax[row][0])
    plot([-5,-width,-width,width,width,5],[0,0,0.5/width,0.5/width,0,0],"k")
    ylim(-0.02,1.1)
    UnBox()
    xticks([])
    yticks([])
    if row: xlabel(r"$\tau$")
    ylabel(r"$F({\bf u},\nu)$")
    
    sca(ax[row][1])
    x=linspace(-23*pi,23*pi,300)
    plot(x,cos(x)*sin(x*width*0.1)/(x*width*0.1),"k")
    UnBox()
    xticks([])
    yticks([])
    if row: xlabel(r"$\tau$")
    ylabel(r"$i(\tau)$")
    SaveFigure("coherence-length.pdf")
