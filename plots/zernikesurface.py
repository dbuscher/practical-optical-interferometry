#!/usr/bin/env python
import os
from plotTools import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

def ZernikeSequence(x,y,numZernike=21,epsilon=1e-10):
    """
    Return Zernike values at a given set of x,y coords up to some maximum 
    Noll index (this version only works up to fifth radial order)
    """
    if numZernike>21:
        raise ValueError('Code for higher radial orders not implemented')
    # Derive radius and exp(i*theta) 
    temp = x + 1j*y
    r1 = np.abs(temp)
    e1 = temp/(r1+epsilon)
     # Generate powers of r recursively
    r2 = r1*r1
    r3 = r2*r1
    r4 = r3*r1
    r5 = r4*r1
    # Generate cos and sin terms recursively from exp(i*theta)
    e2 = e1*e1
    e3 = e2*e1
    e4 = e3*e1
    e5 = e4*e1
    ctheta = e1.real
    stheta = e1.imag
    c2theta = e2.real
    s2theta = e2.imag
    c3theta = e3.real
    s3theta = e3.imag
    c4theta = e4.real
    s4theta = e4.imag
    c5theta = e5.real
    s5theta = e5.imag
    # Generate all the zernikes
    zernike = np.zeros((21,)+x.shape )
    zernike[0] =  1.0
    zernike[1] =  2.0*r1*ctheta
    zernike[2] =  2.0*r1*stheta
    zernike[3] =  sqrt(3.0)*(2.0*r2 - 1.0)
    zernike[4] =  sqrt(6.0)*r2*s2theta
    zernike[5] =  sqrt(6.0)*r2*c2theta
    zernike[6] =  sqrt(8.0)*(3.0*r3 - 2.0*r1)*stheta
    zernike[7] =  sqrt(8.0)*(3.0*r3 - 2.0*r1)*ctheta
    zernike[8] =  sqrt(8.0)*r3*s3theta
    zernike[9] = sqrt(8.0)*r3*c3theta
    zernike[10] = sqrt(5.0)*(6.*r4 - 6.*r2 + 1.)
    zernike[11] = sqrt(10.)*(4.*r4 - 3.*r2)*c2theta
    zernike[12] = sqrt(10.)*(4.*r4 - 3.*r2)*s2theta
    zernike[13] = sqrt(10.)*r4*c4theta
    zernike[14] = sqrt(10.)*r4*s4theta
    zernike[15] = sqrt(12.)*(10*r5-12*r3+3*r1)*ctheta
    zernike[16] = sqrt(12.)*(10*r5-12*r3+3*r1)*stheta
    zernike[17] = sqrt(12.)*(5*r5-4*r3)*c3theta
    zernike[18] = sqrt(12.)*(5*r5-4*r3)*s3theta
    zernike[19] = sqrt(12.)*r5*c5theta
    zernike[20] = sqrt(12.)*r5*s5theta
    # Make zernike zero outside unit circle (useful for dot product)
    zernike = zernike*np.less_equal(r1, 1.0)
    return(zernike[:numZernike])

n_angles = 36
n_radii = 8

# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = np.linspace(0.125, 1.0, n_radii)

# An array of angles
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# Repeat all angles for each radius
angles = np.repeat(angles[...,np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

nx,ny=3,3
fig = plt.figure()
zernikes=ZernikeSequence(x,y)
for j in range(nx*ny):
    ax = fig.add_subplot(nx,ny,j+1, projection='3d')
    plt.title("$Z_"+str(j+1)+"$")
    z = zernikes[j]
    ax.plot_trisurf(x, y, z, color="gray", linewidth=0.2,shade=False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
#plt.tight_layout()
ShowOrSave()
