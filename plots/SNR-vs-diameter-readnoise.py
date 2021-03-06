from plotTools import *

data=ascii.read(DataFilePath("fibre-results.txt")).group_by("numRemove")
figure(figsize=(10,5))
ax=subplot(1,2,1)
for t in data.groups:
    dr0=t["d/r0"]
    rawSNR=t["Vsq"]*dr0**4
    loglog(dr0,rawSNR,color="k")
ScalarLogAxes(yscalar=False)
xlabel(r"$D/r_0$")
ylabel("SNR")
xlim(0.3,30)
ylim(0.1,5e3)

subplot(1,2,2,sharey=ax)
for t in data.groups:
    dr0=t["d/r0"]
    fiberSNR=(t["couple"]*dr0**2)**2
    loglog(dr0,fiberSNR,color="k")
xlim(0.3,30)
ylim(0.1,5e3)
xlabel(r"$D/r_0$")
ScalarLogAxes(yscalar=False)
ShowOrSave()
