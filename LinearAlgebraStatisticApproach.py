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
