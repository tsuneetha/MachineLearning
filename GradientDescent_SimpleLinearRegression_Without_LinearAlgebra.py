#Gradient Descenet algorithm for SIMPLE LINEAR Regression without linear Algebra
import numpy as np
x=np.array([1,2,3,4,5,6])
y=np.array([2.3,9,6.1,7.93,9.98,11.25])
#y=a+bx
#Initialization of weights bias(a) and slope(b)
a=0
b=0
def predict(x,a,b):
    ycap=a+b*x
    return ycap
def loss(y,ycap):
    return ((y-ycap)**2).mean()
def grad_a(y,ycap):
    return (y-ycap).mean()
def grad_b(y,ycap):
    return (x*(y-ycap)).mean()
#Trail 1
ycap=predict(x,a,b)
print(ycap)
loss(y,ycap)
#Finding Gradients
da=grad_a(y,ycap)
db=grad_b(y,ycap)
#Adjusting weights
a+=da*0.02
b+=db*0.02
print(a,b)
#Trail 2
ycap=predict(x,a,b)
print(ycap)
loss(y,ycap)
#Finding Gradients
da=grad_a(y,ycap)
db=grad_b(y,ycap)
#Adjusting weights
a+=da*0.02
b+=db*0.02
print(a,b)
#after weights adjusted, loss got decreased. This is the confirmation for data scaling and change in learning rate not required.
#now we can train the model
#sometimes loss will be increased then Scaling is required.If still loss increased, then learning rate should be decreased.
def train(x,y,w,alpha,iter,conv=1e-9):
    ploss=0
    flag=0
    a=w[0]
    b=w[1]
    for i in range(iter):
        ycap=predict(x,a,b)
        closs=loss(y,ycap)
        diff=abs(closs-ploss)
        if(diff<=conv):
            print("Training completed after ",i+1, "iterations")
            flag=1
            break
        if(i%1000)==0:
            print("loss at iteration",i+1,closs)
        da=grad_a(y,ycap)
        db=grad_b(y,ycap)
        a+=da*alpha
        b+=db*alpha
        ploss=closs
    if(flag==0):
        print("Training not complted run few more iterations")
    return(a,b)
a=0
b=0
w=train(x,y,[a,b],0.02,10000)
print(w)

