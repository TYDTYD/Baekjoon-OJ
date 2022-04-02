import sys
input=sys.stdin.readline

n=int(input())
index=list(map(int,input().split()))
T=sorted(index)
idx=0
idx1=[]
idx2=[]
locate=-1
locatea=0
locatec=0
a=0
b=0
c=1
d=1

while(c<=n-1):
    if a==0:
        idx1.append(abs(T[a]-T[c]))
        locate=a
        locatea=T[a]
        locatec=T[c]
    elif min(idx1)>abs(T[a]-T[c]):
        idx=0
        idx1.append(abs(T[a]-T[c]))
        locate=a
        locatea=T[a]
        locatec=T[c]
    elif min(idx1)==abs(T[a]-T[c]) and locate!=a-1:
        print(locate,a)
        idx=-1
    a=a+1
    c=c+1

T.remove(locatea)
T.remove(locatec)

while(d<len(T)):
    if idx==-1:
        print(0)
        break
    elif b==0:
        idx2.append(abs(T[b]-T[d]))
    elif min(idx1)>abs(T[b]-T[d]):
        idx2.append(abs(T[b]-T[d]))
    b=b+1
    d=d+1

if idx==0:
    if min(idx1)>min(idx2):
        print(min(idx1)-min(idx2))
    else:
        print(min(idx2)-min(idx1))