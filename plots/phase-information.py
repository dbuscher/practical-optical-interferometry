from plotTools import *
from matplotlib.image import imread

def CropImage(image,left,top,width=400,height=400):
    return image[top:top+height,left:left+width]
def PlotImage(img):        
    figure(figsize=(5,5))
    subplot(1,1,1,aspect='equal',frameon=False, xticks=[], yticks=[])
    imshow(img,cmap=cm.gray)
def SwapPhase(image1,image2):
    spec1=fft2(image1)
    phasor=spec1/abs(spec1)
    spec2=fft2(image2)
    amp=abs(spec2)
    return ifft2(amp*phasor).real

fiz=CropImage(imread(DataFilePath('Hippolyte_Fizeau.jpg')),0,5)
# Convert colour to monochrome
fiz=sum(fiz,axis=-1) 
PlotImage(fiz)
SaveFigure("fizeau.pdf")

mich=CropImage(imread(DataFilePath('Albert_Abraham_Michelson2.jpg')),0,20)
PlotImage(mich)
SaveFigure("michelson.pdf")

PlotImage(SwapPhase(mich,fiz))
SaveFigure("michelson-phase.pdf")

PlotImage(SwapPhase(fiz,mich))
SaveFigure("fizeau-phase.pdf")

