from plotTools import *
from AiryPattern import Jinc

fig, ax = pl.subplots(1)
UnBox()
x=np.linspace(0,3,200)
y=Jinc(x*pi)
ax.plot(x,y,linewidth=1.4)
ax.plot(x,x*0,linewidth=1)
pl.ylim(-0.25,1.05)
pl.yticks([0.0,1])
pl.xticks([0,1.22])
pl.xlabel(r"$\theta_d |{\bf u}|$")
pl.ylabel(r"$V({\bf u})$")
Monochrome()
SaveFigure("discvis.pdf")
