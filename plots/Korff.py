#!/usr/bin/env python
# Calculate mean vsquared using Korff's integrals
from scipy.integrate import quad
from numpy import exp,sqrt,array,arange,linspace,logspace,pi,arccos


def timeintegrand(x,tau):
     return(1.-x/tau)*exp(-x**(5./3.))

def VsqTau(tau):
    """Return the mean squared visibility for a separated element
    interferometer with integration time T=tau*t0"""
    result=quad(timeintegrand,0.0,tau,args=(tau,))
    y=result[0]
    return 2*y/tau


def plotSnrTau(min=-1.0,max=1.5,numPoint=100):
    taulist=logspace(min,max,numPoint,endpoint=True)
    y=array([vsqTau(tau) for tau in taulist])
    ax=pl.axes()
    pl.semilogx(taulist,y*sqrt(taulist))
    ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())

def spaceintegrand(r,d):
    a=r/d
    overlap=arccos(a)-a*sqrt(1.-a*a)
    if r<5.0:
        return overlap*r*exp(-6.88*r**(5./3.))
    else:
        return 0.0

def VsqDia(dia):
    """Return the mean squared visibility for a separated element
    interferometer with D/r0=dia"""
    result=quad(spaceintegrand,0.0,dia,args=(dia,))
    y=result[0]
    return 4.0*y/(pi*dia**2/4.0)

def plotVsqDia(min=-1.0,max=1.0,numPoint=100):
    dialist=logspace(min,max,numPoint,endpoint=True)
    y=array([VsqDia(dia) for dia in dialist])
    ax=pl.axes()
    pl.loglog(dialist,y)
    ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    pl.xlabel(r"Diameter/$r_0$")
    pl.ylabel(r"$\langle V^2\rangle$")
