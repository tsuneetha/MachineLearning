#Step1: Prepare Feature and Label matrices
f=open("D:/mystuff/patients.txt")
h=f.readline()
lines=f.readlines()
x=[]
y=[]
for line in lines:
	w=line.strip().split(",")
	ins=[float(v) for v in w[1:-1]]
	x.append(ins)
	if(w[-1]=="yes"):
		y.append(1)
	else:
		y.append(0)
#Feature matrix should be double dimension. and label matrix should be single dimension only
import numpy as np
X=np.array(x)
X.ndim
X.shape
#Step2: Import Classifying models
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.SVM mport SVC
# Creation of Model Object
nb=GaussianNB()
dt=DecisionTreeClassifier()
rf=RandomForestClassifier()
sv=SVC()
#Step3: Train Model
nb.fit(X,y)
dt.fit(X,y)
rf.fit(X,y)
sv.fit(X,y)
#Step 4: Accuracy Testing
nbcap=nb.predict(X)
dtcap=dt.predict(X)
rfcap=rf.predict(X)
svcap=sv.predict(X)
from sklearn.metrics import accuracy_score
accuracy_score(nb,nbcap)
accuracy_score(dt,dtcap)
accuracy_score(rf,rfcap)
accuracy_score(sv,svcap)
#Apply predictions on new data with selected model
file=open("D:/mystuff/newpats.txt")
h=file.readline()
data=file.readlines()
x=[]
for d in data:
  w=d.strip().split(",")
  inputs={float(v) for v in w[1:]
  x.append(inputs)
X=np.array(x)
result=nb.predict(X)
