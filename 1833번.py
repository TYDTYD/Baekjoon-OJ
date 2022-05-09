import sys
input=sys.stdin.readline

def find_parent(parent,x): # 각 원소의 대표 원소를 찾는 함수
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b): # a와 b의 대표 원소를 하나로 정해주는 함수
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b: # a가 더 작다면
        parent[b]=a # b의 대표 원소를 a로
    else: # b가 더 작다면
        parent[a]=b # a의 대표 원소를 b로

n=int(input())
parent=[0]*(n+1)
edges=[]
result=0
c=0

for i in range(1,n+1):
    parent[i]=i # 각 원소마다 자기 번호를 가지고 있도록

for i in range(n):
    city=list(map(int,input().split()))
    for j in range(i,n):
        if i!=j:
            edges.append((city[j],i+1,j+1))
            edges.append((city[j],j+1,i+1))
            if city[j]<0: # 가중치가 음수일 경우
                c-=city[j]

edges.sort()
count=0
new=[]

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b): # 사이클 판별(두 원소의 대표 원소가 같지 않다면)
        if cost<0: # 가중치가 음수라면 이미 설치되어 있으므로
            union_parent(parent,a,b) 
        else:
            union_parent(parent,a,b)
            new.append((a,b))
            count+=1
            result+=cost

print(result+c,count)
for i in range(count):
    print(new[i][0],new[i][1])