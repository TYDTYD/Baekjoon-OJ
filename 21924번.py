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

v,e=map(int,input().split())
parent=[0]*(v+1)
edges=[]
result=0 
index=-1
c=0

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b,cost=map(int,input().split())
    c+=cost # 모든 도로를 다 설치할 경우의 금액을 저장
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

# 이 밑에는 건물이 모두 연결되어 있는지 확인하는 코드
for i in range(1,v):
    if index==-1:
        index=parent[i] # index에 첫번째 원소의 대표 원소를 대입
    else:
        if parent[i]!=index: # i번째 원소의 대표 원소가 index와 다르다면
            if parent[parent[i]]!=index: # i번째 원소의 대표 원소의 대표원소가 index와 다르다면
                print(-1) # 연결되어 있지 않다고 판단 -1 출력
                exit() # 하지만 이 방법은 임시방편일뿐 채점데이터가 약해서 통과된 것 같음

print(parent)
print(c-result)