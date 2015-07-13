from DftAnalysis import *

figure(figsize=(6,4))
summedFringe=sum(FringePatterns(),axis=0)
plot(summedFringe,color="k")
ylabel("intensity")
xlabel("pixel")
UnBox()
ShowOrSave()
