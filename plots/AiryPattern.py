import numpy as np
from NumUtil import CircularMask,Radius
import scipy.special

def Jinc(x,epsilon=1e-6):
    """Return the amplitude of the diffraction pattern of a circular aperture"""
    x2=np.where(np.abs(x)<epsilon,epsilon,x)
    return 2*scipy.special.j1(x2)/x2


def AiryImage(nx,ny,radius,centre=None):
    x=Radius(nx,ny,centre=centre)
    return Jinc(x/float(radius)*1.22*np.pi)**2

def AiryOverlap(nx,ny,radius,offset):
    cx, cy=(nx-1)/2.0,(ny-1)/2.0
    return AiryImage(nx,ny,radius,[cx+offset/2.0,cy])+AiryImage(nx,ny,radius,[cx-offset/2.0,cy])
