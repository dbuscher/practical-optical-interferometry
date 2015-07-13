#!/usr/bin/env python
from plotTools import *

def SplitTable(t,colName):
    # Split a table into sections with common values of column named "colName"
    col=t[colName]
    return [t[col==value] for value in np.unique(col)]

def plotit(dr0,vsq,nrem,plot=plt.loglog,labelval=0.15,lineAnnotate=True):
    """Plot a vsq line with the nrem label in the line"""
    plot(dr0,vsq,label="$n = %d$" % (nrem,),lw=1.5,color="k")
    ypoint=labelval+0.07*nrem
    xpoint=interp(ypoint,vsq[::-1],dr0[::-1])
    if lineAnnotate:
        annotate('n={:d}'.format(nrem), (xpoint,ypoint), ha='center', 
                 va='center', bbox=dict(fc='white', ec='none'))

pysim=SplitTable(ascii.read(DataFilePath("visibility-ao.dat")),
                 "numRemove")
uncorrected=ascii.read(DataFilePath("visibility-uncorrected.dat"),guess=False,Reader=ascii.CommentedHeader)
figure(figsize=(6*1.1,4*1.1))
ls=LineStyleCycler()
#FastText()
plotit(uncorrected["D"],uncorrected["V"]**2,0)
for n,sim in enumerate(pysim[:]):
    numRemove=sim["numRemove"][0]
    dr0=sim["d/r0"]
    vsq=sim["Vsq"]
    plotit(dr0,vsq,n+1,lineAnnotate=(n<2))
plt.xlabel(r"$D/r_0$")
plt.ylabel(r"$\left\langle\left|\gamma^2\right|\right\rangle$")
plt.xlim(0.1,10)
plt.ylim(0.08,1.1)
ScalarLogAxes()
SaveFigure("aovisibility.pdf")
