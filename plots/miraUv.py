from plotTools import *

def plotit(fname=DataFilePath("miraUV.dat"),
           labels=["A1-B2","B2-C1","C1-D0","A1-D0","A1-C1","B2-D0"],
           sampling=4):
    data=ascii.read(fname)
    markercycle=itertools.cycle(markers)
    for icol,label in enumerate(labels):
        u=data["col"+str(icol*2+1)][::sampling]
        v=data["col"+str(icol*2+2)][::sampling]
        marker=next(markercycle)
        plt.scatter(u,v,s=1)
        plt.scatter(-u,-v,s=1)
        plt.xlim(-35,35)
        plt.ylim(-35,35)
        plt.axes().set_aspect('equal', 'datalim')
        plt.xlabel("u (m)")
        plt.ylabel("v (m)")

plotit()
ShowOrSave()
