from plotTools import *
from NumUtil import CircularMask

import matplotlib.patches as patches

def PupilFringes(numPix, V,freq=8.0):
    fringe=1.0+(V*np.sin(np.arange(numPix)*2*np.pi*freq/numPix)).real
    mask=CircularMask(0.5*(numPix-1),numPix,numPix)
    return mask*fringe+2.0*(1.0-mask)

def PlotPupilFringes(numPix=200, vList=[1.0,0.5,0.1]):
    fig = pl.figure(figsize=(6,2))
    numCol=len(vList)
    for iPlot,V in enumerate(vList):
        ax = fig.add_subplot(1,numCol,iPlot+1,
                             aspect='equal',frameon=False, xticks=[], yticks=[])
        im = ax.imshow(PupilFringes(numPix,V),vmin=0.0,vmax=2.0,cmap=pl.cm.gray)
        ax.set_title(r"$|V|=%3.1f$"%V, fontsize=16)
        #patch = patches.Circle((300,300), radius=100)
        #im.set_clip_path(patch)
        
PlotPupilFringes()
SaveFigure("fringecontrast.pdf")

