from plotTools import *

def PhotonDegeneracy(alpha): return(1.0/(exp(alpha)-1))

figure(figsize=(5,10/3))
x=logspace(-1.5,1.3,100)
y=PhotonDegeneracy(x)
loglog(x,y,color="k")
xlim(0.03,20)
ylim(1e-6,100)
ScalarLogAxes(yscalar=False)
ylabel("degeneracy parameter")
xlabel(r"$h\nu/kT$")
yticks([1e2,1,1e-2,1e-4,1e-6])
SaveFigure("degeneracyparameter.pdf")
