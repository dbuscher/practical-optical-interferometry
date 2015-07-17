#!/usr/bin/env python
#
# Functions to calculate the refraction of air and derived quantities
# relevant to air paths in an interferometer.

import math
import numpy as np

class Air:
    def __init__(self,p=1013.25, T=293.15, e=0.0):
        """
        p: millibar of total air pressure
        T: Kelvin
        e: millibar partial water vapour pressure
        """
        self.p=p
        self.T=T
        self.e=e
    def Mu(self,wavelength):
        """
        Calculates the refractivity (n-1) of air.
        Inputs: wavelength/microns

        result: metres/metre of air
        """
        k = 1./(wavelength*wavelength)
        a = 1.e-8*( 2372.434 + 684255.24/(130.-k) + 4549.40/(38.9-k) )
        b = a - 1.e-8*(6487.31 +k*( 58.058 +k*(-0.71150 +k*0.08851 ) ) )
        return ( a*self.p - b*self.e ) / self.T

def GroupDelayRefractivity(medium,wavelength,delta=1e-4):
    """
    Calculates the quantity (n-1)-lambda*(dn/dlambda) for air
    at a given wavelength, where lambda is in microns.
    This is equal to the change in the zero group delay position
    when 1 metre of vacuum path is replaced with 1 metre of air.
    Units:
    wavelength: microns
    result: metres per metre of air path difference.
    """
    return(DispersiveDelay(medium,wavelength,delta)
           + medium.Mu(wavelength))

def DispersiveDelay(medium,wavelength,delta=1e-4):
    return (medium.Mu(wavelength)-medium.Mu(wavelength*(1.0+delta)))/delta


