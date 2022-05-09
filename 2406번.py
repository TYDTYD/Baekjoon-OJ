import sys
input=sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)
edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    x,y=map(int,input().split()) # 연결되어 있는 컴퓨터들은 
    union_parent(parent,x,y) # 연결해 놓는다

for i in range(n):
    city=list(map(int,input().split()))
    for j in range(i,n):
        if i!=j and i!=0: # 첫번째 줄은 무시한다 어차피 다른 컴퓨터들과 다 연결되어 있기 때문에
            edges.append((city[j],i+1,j+1))
            edges.append((city[j],j+1,i+1))

edges.sort()
count=0
new=[]

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        new.append((a,b))
        count+=1
        result+=cost

if count==0: # 안정적인 네트워크일 경우
    print(0,0)
else:
    print(result,count)
    for i in range(count):
        print(new[i][0],new[i][1])