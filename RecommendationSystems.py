f=open("C:/Users/ic762755/Desktop/mystuff/friends.txt")
lines=f.readlines()[1:]
print(lines)
flist=[]
for line in lines:
    w=line.strip().split(",")
    u=w[0]
    f=w[1]
    flist.append([u,f])
    flist.append([f,u])
print(flist)
friends={}
for f in flist:
    u=f[0]
    fr=f[1]
    if friends.get(u)==None:
        friends[u]=[fr]
    else:
        friends[u].append(fr)
print(friends)
#Common Friends
def common(x,y):
    com=[]
    for v in x:
        if v in y:
            com.append(v)
    return com
#Building Recommendations
def recommendations(x,y):
    rec=[]
    for v in x:
        if v not in y:
            rec.append(v)
    return rec
u=["ravi","sunita","phani","Jashu","Ramana","Venky","Reddy"]
me=["phani","Jashu","Ramana","siri","Alexa"]
#common(u,me)
recommendations(u,me)
recommendations(me,u)
print(friends)
rec={}
for k in friends:
    rlist=[]
    kf=friends[k]
    print(kf)
    for f in kf:
        rlist+=recommendations(friends[f],kf)
    fr=[v for v in rlist if v!=k]
    rec[k]=list(set(fr))
print(rec)
out=open("C:/Users/ic762755/Desktop/mystuff/newfriends.txt","w")
hdr='User\tPeople you may know\n'
out.write(hdr)
for i in rec:
    rlist=rec[i]
    line=i+"\t"+",".join(rlist)+"\n"
    out.write(line)
out.close()
