from DftAnalysis import *

figure(figsize=(6*0.6,4*0.6))
offset=0.08
newx=[]
newy=[]
for i in range(10):
    newx+=[i-offset,i,i+offset]
    newy+=[0,f(i),0]
plot(newx,newy,color='0.0')
x=linspace(0,10,100)
y=f(x)
plot(x,y,color='0.5')
xlim(0,10)
xlabel("$x$")
ylabel("$f(x)$")
UnBox()
ShowOrSave()
