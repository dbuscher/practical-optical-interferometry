#!/usr/bin/env python
from plotTools import *

def SplitTable(t,colName):
    # Split a table into sections with common values of column named "colName"
    col=t[colName]
    return [t[col==value] for value in np.unique(col)]

def plotit(dr0,vsq,nrem,plot=plt.loglog,labelval=0.15):
    """Plot a vsq line with the nrem label in the line"""
    plot(dr0,vsq,label="$n = %d$" % (nrem,),lw=1.5,color="k")
    ypoint=labelval+0.05*nrem
    xpoint=interp(ypoint,vsq[::-1],dr0[::-1])
    if nrem<3: annotate('n={:d}'.format(nrem), (xpoint,ypoint), ha='center', 
                        va='center', bbox=dict(fc='white', ec='none'))

pysim=SplitTable(ascii.read(DataFilePath("visibility-ao.dat")),
                 "numRemove")
figure(figsize=(6*1.1,4*1.1))
ls=LineStyleCycler()
for n,sim in enumerate(pysim[:]):
    numRemove=sim["numRemove"][0]
    dr0=sim["d/r0"]
    couple=sim["meanCouple"]
    plotit(dr0,couple,n+1)
#    vsq=sim["Vsq"]
#    plotit(dr0,sqrt(vsq),n+1)
plt.xlabel(r"$D/r_0$")
plt.ylabel(r"Mean coupling")
plt.xlim(0.1,10)
plt.ylim(0.08,1.1)
ScalarLogAxes()
SaveFigure("aofiber.pdf")
