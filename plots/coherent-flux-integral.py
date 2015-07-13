from plotTools import *
def Gaussian(x,sigma): return exp(-x**2/(2.0*sigma**2))/sigma
x=np.linspace(-4,4,200)
plot(x,Gaussian(x,0.2),color="k")
plot(x,Gaussian(x,0.8),color="0.5")
plot(x,cos(2*pi*x),color="k",ls="dotted")
UnBox()
ylabel("$I(\sigma)$")
xlabel("$u\sigma$")
xlim(-4,4)
ylim(-1.5,5.5)
xticks([-2,0,2])
yticks([])
SaveFigure("coherent-flux-integral.pdf")
