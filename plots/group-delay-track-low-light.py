from plotTools import *
from GroupDelaySimulation import PlotGroupDelaySimulation

phase=np.loadtxt(DataFilePath("phase-sequence.txt"))
PlotGroupDelaySimulation(phase[:64000],SNR=1.0)
ShowOrSave()

