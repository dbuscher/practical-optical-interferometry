from UvEllipse import *

n=8
min=-105
max=min+15*n

ha=linspace(deg2rad(min),deg2rad(max),n,endpoint=True)
plotEllipse(ha)
SaveFigure("earth-rotation-partial.pdf")
