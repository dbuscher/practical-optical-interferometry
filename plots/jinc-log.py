from plotTools import *
import scipy.special

def Jinc(x,epsilon=1e-6):
    """Return the amplitude of the diffraction pattern of a circular aperture"""
    x2=np.where(np.abs(x)<epsilon,epsilon,x)
    return 2*scipy.special.j1(x2)/x2

x=linspace(0,6,100)
semilogy(x,abs(Jinc(x*pi)),color="k")
ylim(7e-3,1)
xlabel("Baseline")
ylabel("Visibility")
xticks([1,3,5],[r"$\lambda/\theta_{\rm d}$",
                    r"$3\lambda/\theta_{\rm d}$",
                    r"5$\lambda/\theta_{\rm d}$",])
ShowOrSave()
