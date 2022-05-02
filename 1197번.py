import sys
import heapq
input=sys.stdin.readline
INF=10**12

v,e=map(int,input().split())
graph=[[] for _ in range(v)]
d=[INF]*v
Q=[]
visited=[False]*v

for i in range(v):
    Q.append(i)

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

def Prim(graph,start):
    d[start]=0
    h=[]
    heapq.heappush(h,(0,start))
    while Q:
        w,u=heapq.heappop(h)
        if visited[u]:
            continue
        Q.remove(u)
        visited[u]=True
        for i in graph[u]:
            if not visited[i[0]] and i[1]<d[i[0]]:
                d[i[0]]=i[1]
                heapq.heappush(h,(i[1],i[0]))
    return sum(d)

print(Prim(graph,0))