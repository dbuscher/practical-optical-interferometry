#!/usr/bin/env python
from plotTools import *
from air import Air,GroupDelayRefractivity

wav=np.linspace(0.45,2.4,200)
air=Air()

figure(figsize=(6,4))
#FastText()
plot(wav*1000,air.Mu(wav)*1e6,color="k")
xlim(400,2300)
ylim(267.5,274.5)
xlabel("Vacuum wavelength (nm)")
ylabel("Refractivity (ppm)")
SaveFigure("refractivity.pdf")
