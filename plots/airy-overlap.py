from plotTools import *
from AiryPattern import AiryOverlap

def PlotAiryOverlap(numPix=500, radius=100, separations=[2.0,1.0,0.5,0.1]):
    numCol=len(separations)
    fig = pl.figure(figsize=(numCol*2,2))
    for iPlot,offset in enumerate(separations):
        ax = fig.add_subplot(1,numCol,iPlot+1,
                             aspect='equal',
                             frameon=False,
                             xticks=[], yticks=[])
        y=AiryOverlap(numPix,numPix,radius,offset*radius)
        im = ax.imshow(sqrt(y),cmap=pl.cm.gray)
        ax.set_title(r"$\Delta\theta=%3.1f\lambda/d$"%offset, fontsize=16)
PlotAiryOverlap()
SaveFigure("airy-overlap.pdf")
