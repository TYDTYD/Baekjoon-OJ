from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

result=[0]*(n+1)
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
recur=[[] for _ in range(n+1)]
basic=[False]*(n+1)

for i in range(1,m+1):
    x,y,k=map(int,input().split())
    indegree[x]+=1
    graph[y].append((x,k))
    recur[x].append((y,k))

q=deque()

for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
        basic[i]=True

while q:
    index=q.popleft()
    for i in graph[index]:
        indegree[i[0]]-=1
        if basic[index]:
            result[index]+=i[1]
        else:
            result[index]*=i[1]
        if indegree[i[0]]==0:
            q.append(i[0])

for i in range(1,n+1):
    if result[i]!=0:
        print(i,result[i])