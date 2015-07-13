#!/usr/bin/env python
import os
from os.path import dirname,abspath
os.sys.path.insert(0,dirname(dirname(abspath(__file__))))
from plotTools import *
fig=figure(figsize=(8,8))
ax = fig.add_subplot(111,aspect='equal',frameon=False, xticks=[], yticks=[])
x, y= 0.0,0.0
np.random.seed(5)
angles=360*np.random.uniform(size=(8,))
scale=1.0
for degrees in angles:
    radians=degrees/180.*pi
    dx=scale*cos(radians)
    dy=scale*sin(radians)
    arrow( x, y, dx, dy, fc="k", ec="k",
           head_width=0.15, head_length=0.2,length_includes_head=True)
    x+=dx/scale
    y+=dy/scale
angle=arctan2(y,x)
arrow( 0,0, x, y, fc="k", ec="k",
       head_width=0.1, head_length=0.2,lw=2,length_includes_head=True)
dscale=0.93
arrow( 0,0, dscale*x, dscale*y, fc="k", ec="k",
       head_width=0.1, head_length=0.2,lw=2,length_includes_head=True)
#text(x-0.5,y+0.5,"Vector average",horizontalalignment='left',
#     verticalalignment='center',)
# Do axes
xamax=2
xamin=-2
yamax=xamax
yamin=xamin
arrow(xamin,0,xamax-xamin,0,
      head_width=0.1, head_length=0.2,overhang=0.5,fc="k", ec="k",)
arrow(0,yamin,0,yamax-yamin,head_width=0.1, head_length=0.2,overhang=0.5,fc="k", ec="k",)
text(xamax+0.5,0,"Real",horizontalalignment='left',
     verticalalignment='center',)
text(0,yamax+0.5,"Imaginary",horizontalalignment='center',
     verticalalignment='bottom',)

xlim(-6,6)
ylim(yamin,yamax+1)
SaveFigure("randomwalk.pdf")
