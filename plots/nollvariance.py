#!/usr/bin/env python
from plotTools import *
from scipy.special import gamma

def NollCovariance(ni,nj,m=None):
    """Return covariance of Zernikes of radial order n{i,j} and azimuthal
    order m.  Note that if m_j != m_i then the correlation is zero. 
    Does not check if m is allowed"""
    if m==None:
        m=ni%2
    return (0.0072*(-1)**((ni+nj-2*m)/2)*np.sqrt((ni+1)*(nj+1))*pi**(8./3)
            *gamma(14./3.)*gamma((ni+nj-5./3)/2)/
            (gamma((ni-nj+17/3.)/2)*gamma((nj-ni+17./3)/2)*
             gamma((ni+nj+23/3.)/2)))

n=np.arange(1,10)
nmode=n+1
variance=NollCovariance(n,n)*nmode
plt.semilogy(n,variance,marker=markers[1],color="k")
plt.xlabel("Zernike radial order")
plt.ylabel("Variance")
ShowOrSave()
