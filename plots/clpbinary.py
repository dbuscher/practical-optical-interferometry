#!/usr/bin/env python
from plotTools import *
from NumUtil import *

def visbinary(ratio,u):
    return 1+ratio*exp(1j*2*pi*u)

u=np.linspace(-1.0,1.0,100)
ratio=0.1
v12=visbinary(ratio,u)
v23=visbinary(ratio,2*u)
v31=visbinary(ratio,-3*u)
tp=v12*v23*v31
figure(figsize=(6,4))
plot(u,np.angle(v12),lw=1,ls="dashed",color="black",label=r"$\phi_{12}$")
plot(u,np.angle(v23),lw=1,ls="dotted",color="black",label=r"$\phi_{23}$")
plot(u,np.angle(v31),lw=1,ls="dashdot",color="black",label=r"$\phi_{31}$")
plot(u,np.angle(tp),lw=1.5,color="black",label=r"$\Phi_{123}$")
ylim(-0.3,0.65)
legend(loc="upper right")
xlabel(r"$u_0\Delta\theta$")
ylabel("Closure phase (radians)")
SaveFigure("clpbinary.pdf")
