from plotTools import *
def Baselines(stationX, stationY):
    return (subtract.outer(stationX,stationX).flat,
            subtract.outer(stationY,stationY).flat,)

def MakeWye(stationsPerArm,armLength,angles=(pi/2, 7*pi/6.,-pi/6.)):
    d=arange(1,stationsPerArm+1)*float(armLength)/stationsPerArm
    x=concatenate([zeros((1,))]+ [ cos(angle)*d
                                   for angle in angles])
    y=concatenate([zeros((1,))]+ [ sin(angle)*d
                                   for angle in angles])
    return x,y
greyscalePlotScheme=[(3,'0.0'),(2,'0.5'), (1,'0.75')]
colourPlotScheme=[(3,"c"),(2,"b"),(1,"r")]
def PlotTelescopes(plotScheme=greyscalePlotScheme):
    for n, color in plotScheme:
        x,y=MakeWye(n,7.8*n)
        scatter(x,y,s=40,marker="o",edgecolors="k",facecolors=color,
                label="%d tels"%(3*n+1))
    xlabel(r"$x\,{\rm (m)}$")
    ylabel(r"$y\,{\rm (m)}$")
    title("Telescope coordinates")
    xlim([-48,48])
    ylim([-48,48])

def PlotUv(plotScheme=greyscalePlotScheme):
    for n, color in plotScheme:
        x,y=MakeWye(n,7.8*n)
        bx,by=Baselines(x,y)
        scatter(bx,by,s=80,marker="o",edgecolors="k",facecolors=color)
    xlabel(r"$B_x\,{\rm (m)}$")
    ylabel(r"$B_y\,{\rm (m)}$")
    title("Baseline coordinates")
    xlim([-48,48])
    ylim([-48,48])
    
fig = figure(1,figsize=(10,5))
fig.clf()
scheme=[(3,'0.5')]
fig.subplots_adjust(wspace=0.3,left=0.08,right=0.92)
ax=fig.add_subplot(121, aspect="equal", adjustable="box")
PlotTelescopes(plotScheme=scheme)
ax=fig.add_subplot(122, aspect="equal", adjustable="box")
PlotUv(plotScheme=scheme)
ax.yaxis.set_ticks_position("right")
ax.yaxis.set_label_position("right")
savefig("mroi-uv.pdf",transparent=True,bbox_inches="tight")
