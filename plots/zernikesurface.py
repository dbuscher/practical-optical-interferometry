#!/usr/bin/env python
import os
from plotTools import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from zernikeWerkhoven import zernikel


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
for j in range(nx*ny):
    ax = fig.add_subplot(nx,ny,j+1, projection='3d')
    plt.title("$Z_"+str(j+1)+"$")
    z = zernikel(j,np.sqrt(x**2+y**2),np.arctan2(x,y))
    ax.plot_trisurf(x, y, z, color="gray", linewidth=0.2,shade=False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
#plt.tight_layout()
ShowOrSave()
