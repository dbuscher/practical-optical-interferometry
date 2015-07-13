#!/usr/bin/env python
from __future__ import print_function
from plotTools import *

from plot import *

def GenerateAngles(mean,sigma,num):
    np.random.seed(1234)
    angles=mean + sigma*np.random.normal(size=(num,))
    return where(angles>180,angles-360,angles)
def PlotArrows(angles,scale=1.0):
    radians=angles/180.*pi
    dx=scale*cos(radians)
    dy=scale*sin(radians)
    x=0.0
    y=0.0
    for i in range(len(dx)):
         arrow( x, y, dx[i], dy[i], fc="k", ec="k",
               head_width=0.2, head_length=0.4,overhang=0.3,
               length_includes_head=True)
        x+=dx[i]
        y+=dy[i]
    return(x,y)
def PlotDoubleArrow(x,y,dscale=0.93):
    arrow( 0,0, x, y, fc="k", ec="k",
           head_width=0.2, head_length=0.5,overhang=0.5,lw=2,length_includes_head=True)
    arrow( 0,0, dscale*x, dscale*y, fc="k", ec="k",
           head_width=0.2, head_length=0.5,overhang=0.5,lw=2,length_includes_head=True)
    #text(x-0.5,y+0.5,"Vector average",horizontalalignment='left',verticalalignment='center',)


figure(figsize=(10,4))
subplot(121)
angles=GenerateAngles(150,50,12)
hist(angles,bins=20,range=(-180,180),color='0.75')
yticks([1,2,3])
xlim(-180,180)
xlabel("Phase (degrees)")
ylabel("Frequency")
subplot(122,aspect='equal',)


x,y=PlotArrows(angles)
PlotDoubleArrow(x,y)

xlim(-8,0)
ylim(-2.5,4.5)
xlabel("Real")
ylabel("Imagingary")
SaveFigure("vectoraverage.pdf")
print("mean phase",average(angles))
print("vector average",rad2deg(arctan2(y,x)))
