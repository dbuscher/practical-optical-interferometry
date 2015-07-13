#!/usr/bin/env python
from plotTools import *

#rc('text', usetex=True)
rc('font', family='serif')

def CentralSubImage(image,size):
    ny=(image.shape[0]-size)/2
    nx=(image.shape[1]-size)/2
    return image[ny:ny+size,nx:nx+size]

def plot(fname,showSize=100):
    image=fits.open(DataFilePath(fname))[0].data
    s=CentralSubImage(np.sqrt(image),showSize)
    imshow(s,cmap=cm.gray)
#    axes(frameon=False)
    xticks([])
    yticks([])

fig=figure(figsize=(8,8/3.2))
#fig.set_tight_layout(True)
gs = gridspec.GridSpec(1, 3,width_ratios=[1,1,1])
gs.update(wspace=0.1,hspace=0.1)
ax = subplot(gs[0])
plot("airy.fits")
ax = subplot(gs[1])
plot("speckle.fits")
ax = subplot(gs[2])
plot("seeing.fits")
SaveFigure("speckle.pdf")
