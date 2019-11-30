#step 1: Read data from file
f=open("patient.txt")
h=f.readline()
lines=f.readlines()
len(lines)
#Step2: Preapare featire and label Matrices
x=[]
y=[]
for line in lines:
    w=line.strip().lower().split(",")
    ins=w[2:-1]
    inputs=[float(v) for v in ins]
    print(inputs)
    x.append(inputs)
    y.append(float(w[-1]))
print(x)
print(y)
import numpy as np
ones=np.ones(len(lines))
X=np.c_[ones,x]
Y=np.c_[y]
X.shape
Y.shape
#Step 3: Find weights between X,Y
def weights(x,y):
    from numpy.linalg import inv
    return inv(x.T.dot(x)).dot(x.T.dot(y))
w=weights(X,Y)
print(w)
#Step 4: Find Accuracy.Apply prediction on given data
ycap=X.dot(w)
print(np.c_[y,ycap])
def Accuracy(y,ycap,closeness):
    de=100-closeness
    dist=abs(y-ycap)/abs(y)*100
    pcnt=dist[dist<=de].size
    n=y.size
    acc=pcnt/n*100
    return acc
Accuracy(Y,ycap,95)
#read data of new patients and prepare predictable matrix
infile=open("C:/Users/ic762755/Desktop/mystuff/newpatients.txt")
hdr=infile.readline()
data=infile.readlines()
p=[]
for line in data:
    a=line.strip().lower().split(",")
    ins=[float(v) for v in a[2:]]
    p.append(ins)
print(p)
o=np.ones(len(data))
p=np.c_[o,p]
P=np.array(p)
print(P)
print(w)
chols=P.dot(w)
chols
#step7: write results into new file along with inputs
results=np.c_[data,chols.ravel()]
print(results)
out=open("C:/Users/ic762755/Desktop/mystuff/newpatients.txt",'w')
header="'id','name','age','wgt','hgt','cholestrol'"
out.write(header+"\n")
for arr in results:
    line=arr[0].strip()+arr[1]
    out.write(line+"\n")
out.close()
