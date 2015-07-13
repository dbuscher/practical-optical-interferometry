from plotTools import *

data=ascii.read(DataFilePath("visibility-uncorrected.dat"),guess=False,Reader=ascii.CommentedHeader)
d=data["D"]
v=data["V"]
figure(figsize=(9*0.75,6*0.75))
plt.loglog(d,v**2,label=r"Numerical result",color="black")
d0=v[-1]*d[-1]
#print "d0=",d0
plt.loglog(d,exp(-2.06*d**(5./3.)),color="black",lw=1.5,ls="dashed",
           label=r"Extended Maréchal")
plt.loglog(d,(d0/d)**2,color="black",lw=1.5,ls="dotted",
           label=r"Random walk")
#d=np.logspace(-1,log10(0.4),100)
legend(loc="lower left")
plt.xlim(0.05,10)
plt.ylim(9e-3,1.1)
plt.xlabel(r"$D/r_0$")
plt.ylabel(r"$\left\langle\left|\gamma\right|^2\right\rangle$")
#UnBox()
ScalarLogAxes()
ShowOrSave()
