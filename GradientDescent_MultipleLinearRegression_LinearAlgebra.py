#Multiple Linear Regression with Gradient Descent Algorithm in Linear Algebra Style
#more than one input variable
"""
File: Patients.txt
schema: id,name,age,wgt,hgt,cholestral
features:age,wgt,hgt
label: continuous type- cholestarl
"""
#step1: read data and seperate features and labels
f=open("C:/Users/ic762755/Desktop/mystuff/patients.txt")
hdr=f.readline()
data=f.readlines()
x=[]
y=[]
for line in data:
    w=line.strip().lower().split(",")
    ins=[float(v) for v in w[2:-1]]
    x.append(ins)
    y.append(float(w[-1]))
import numpy as np
x=np.array(x)
ones=np.ones(x.shape[0])
X=np.c_[ones,x]
Y=np.c_[y]
print(X)
print(Y)
#Define Random Weights
np.random.seed(90)
w=2*np.random.random((X.shape[1],1))-1
print(w.shape)
#functions for prediction.loss(mse),derivative
def predict(x,w):
    return x.dot(w)
def loss(y,ycap):
    return ((y-ycap)**2).mean()
def derivative(x,y,w):
    ycap=predict(x,w)
    return (x.T.dot(y-ycap))/x.shape[0]
#Step4: perform trails whether loss is decreasing
#trail 1
ycap1=predict(X,w)
print(loss(y,ycap1))
grad=derivative(X,Y,w)
w+=grad*0.02
#trail 2
ycap2=predict(X,w)
print(loss(y,ycap2))
grad=derivative(X,Y,w)
w+=grad*0.02
"""Observation from above trails is instead of decrement of loss, loss got increased. So scaling is required"""
#step 5: Scaling
def sd(x):
    return (((x-x.mean())**2).sum()/(x.size-1))**0.5
def scale(x):
    return (x-x.mean())/sd(x)
def scaleMatrix(x):
    for i in range(x.shape[1]):
        col=x[:,i]
        x[:,i]=scale(col)
    o=np.ones(x.shape[0])
    return np.c_[o,x]
#creating seperate instances for feature and label matrices
ins=np.array(x)
out=np.array(Y)
X=scaleMatrix(ins)
YL=scaleMatrix(out)
YL=out
print(X)
print(YL)
print(ins)
print(out)
#Step 6: Train the Model
def train(x,y,w,alpha,iter,conv=1e-9):
    ploss=0
    flag=0
    for i in range(iter):
        ycap=predict(x,w)
        closs=loss(y,ycap)
        if i%1000==0:
            print("loss at iteration",i+1,closs)
        diff=abs(ploss-closs)
        if(diff<conv):
            print("Training completed after",i+1,"iterations")
            flag=1
            break
        grad=derivative(x,y,w)
        w+=grad*alpha
        ploss=closs
    if(flag==0):
        print("Training not completed run few more iterations")
    return w
theta=np.array(w)
theta=train(X,YL,theta,0.02,1000000)
print(w)
print(theta)
#Step 7: Accuracy testing based on closeness expectation between actual and predicted labels
def accuracy(y,ycap,closeness):
    de=100-closeness
    dist=abs(y-ycap)/abs(y)*100
    pcnt=dist[dist<=de].size
    n=y.shape[0]
    return pcnt/n*100
ycap=predict(X,theta)
print(ycap)
yc=ycap*sd(Y)+Y.mean()
print(yc)
accuracy(Y,yc,95)
np.c_[Y,yc,abs(Y-yc)/abs(Y)*100]
#step 9: Apply predictions on new data
new=open("C:/Users/ic762755/Desktop/mystuff/newpatient.txt")
hd=new.readline()
data=new.readlines()
p=[]
for line in data:
    a=line.strip().lower().split(",")
    ins=[float(v) for v in a[2:]]
    p.append(ins)
P=np.array(p)
print(P)
#Scaling new data with train data mean and standard deviation
for i in range(P.shape[1]):
    s=sd(x[:,i])
    m=x[:,i].mean()
    P[:,i]=(P[:,i]-m)/s
print(P)
o=np.ones(len(data))
P=np.c_[o,P]
pcap=predict(P,theta)
print(pcap)
chols=pcap*sd(Y)+Y.mean()
chols=chols.ravel()
chols
res=[d.strip()+","+str(c) for d,c in list(zip(data,chols))]
res
outfile=open("C:/Users/ic762755/Desktop/mystuff/newpatient.txt",'w')
hdr='"Id","Name","Age","Weight","Height","Cholestrals"'
outfile.write(hdr+"\n")
for line in res:
    outfile.write(line+"\n")
outfile.close()

