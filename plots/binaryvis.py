from plotTools import *

f1=1
f2=0.3
fig = pl.figure(figsize=(10*0.7,4*0.7))
x=linspace(0,3,200)
y=(f1+f2*exp(1j*2*pi*x))/(f1+f2)
ax = fig.add_subplot(1,2,1)
UnBox()
ax.plot(x,abs(y))
pl.xlabel(r"${\bf u}\cdot{\bf\sigma}_0$")
pl.ylabel(r"$\left|V(u)\right|$")
pl.ylim(0.25,1.05)
ax = fig.add_subplot(1,2,2)
UnBox()
ax.plot(x,angle(y,deg=False))
#ax.plot(x,17*sin(2*pi*x))
pl.xlabel(r"${\bf u}\cdot{\bf\sigma}_0$")
pl.ylabel(r"${\rm arg}\left[V({\bf u})\right]$ (radians)")
ylim(-0.35,0.35)
Monochrome()
tight_layout()
SaveFigure("binaryvis.pdf")
