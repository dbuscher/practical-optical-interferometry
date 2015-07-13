from plotTools import *

fig, ax = pl.subplots(2, sharex=True)
UnBox(ax[0])
UnBox(ax[1])
x=linspace(-8*pi,8*pi,200)
sum=zeros_like(x)
for wnum in linspace(0.9,1.1,5):
    y=cos(wnum*x)
    sum+=y
    ax[0].plot(x,y,"k",lw=1.0)
ax[0].set_ylim(-1.2,1.1)
ax[0].set_xlim(-9*pi,9*pi)
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[1].plot(x,sum,"k")
ax[1].set_ylim(-7,7)
ax[1].set_xlabel(r"$\tau$")
ax[1].set_ylabel(r"$i(\tau)$")
ax[0].set_ylabel(r"$i(\tau)$")
#Monochrome()
SaveFigure("polychromatic.pdf")
