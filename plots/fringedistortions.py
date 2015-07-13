#!/usr/bin/env python
from plotTools import *
from NumUtil import CircularMask
from PhaseScreen import ScreenGenerator

def PupilFringes(screen, V,freq=10.0):
    numPix=screen.shape[0]
    fringe=1.0+(V*np.sin(arange(numPix)*2*np.pi*freq/numPix+screen))
    mask=CircularMask(0.5*(numPix-1),numPix,numPix)
    return mask*fringe+2.0*(1.0-mask)

screenSize=512
diameter=200
r0=50.0
np.random.seed(1234)
screenGenerator = ScreenGenerator(screenSize,r0,diameter,diameter)
screen=next(screenGenerator)
fringes=PupilFringes(screen,1.0)
fig=figure()
ax = fig.add_subplot(111,
                     aspect='equal',frameon=False, xticks=[], yticks=[])
ax.imshow(fringes,cmap=cm.gray)
ShowOrSave()

