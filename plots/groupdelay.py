#!/usr/bin/env python
from plotTools import *
from Air import Air,DispersiveDelay,GroupDelayRefractivity

wav=np.linspace(0.45,2.4,200)
air=Air()
g0=GroupDelayRefractivity(air,2.4)

figure(figsize=(6,4))
plot(wav*1000,(GroupDelayRefractivity(air,wav)-g0)*1e6,color="black")
xlim(480,2300)
ylim(-1,20)
xlabel("Vacuum wavelength (nm)")
ylabel("Relative group delay (microns)")
SaveFigure("groupdelay.pdf")
