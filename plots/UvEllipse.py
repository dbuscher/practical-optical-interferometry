from plotTools import *

def UvEllipse(Bpol, Beq, squash, ha):
    u=Beq*sin(ha)
    v=Bpol+Beq*cos(ha)*squash
    return (u,v)


def plotEllipse(ha):
    u,v=UvEllipse(1,3,0.15,ha)
    figure(1,(3,3))
    subplot(111, aspect="equal", adjustable="box")
    for mirror, colour in ((1,'0.5'),(-1,'0.75')):
        scatter(mirror*u,mirror*v,marker="o",edgecolors="k",facecolors=colour)
    xlabel("$u$")
    ylabel("$v$")
    xticks([0])
    yticks([0])
    grid()


