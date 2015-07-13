from plotTools import *

fig, ax = pl.subplots(1)
UnBox(ax)
#FastText()
x=linspace(0,1.2,100)
y=exp(-4*log(2)*(x/0.883)**2)
pl.plot(x,y,color="k")
pl.ylabel(r"$V(|{\bf u}|)$")
pl.xlabel(r"$|{\bf u}|\theta_d$")
SaveFigure("gaussian.pdf")
