import sys
import heapq
input=sys.stdin.readline
INF=10**12

v,e=map(int,input().split())
graph=[[] for _ in range(v)]
d=[INF]*v
Q=[]

for i in range(v):
    Q.append(i)

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

def Prim(graph,start):
    d[start]=0
    while(Q!=[]):
        h=[]
        for i in Q:
            heapq.heappush(h,(d[i],i))
        minimum=heapq.heappop(h)
        Q.remove(minimum[1])
        u=minimum[1]
        for i in graph[u]:
            if i[0] in Q and i[1]<d[i[0]]:
                d[i[0]]=i[1]
    return d

result=Prim(graph,0)
print(sum(result))