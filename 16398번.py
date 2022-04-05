import sys
import heapq
input=sys.stdin.readline
INF=10**12

n=int(input())
graph=[[] for _ in range(n)]
Q=[] # 최소 신장 트리에 속하지 않은 정점 리스트
d=[INF]*n # 가중치 갱신 리스트 (모두 무한대로 시작)

for i in range(n):
    Q.append(i) # 모든 정점 입력

for i in range(n):
    flow=list(map(int,input().split()))
    for j in range(n):
        if i!=j:
            graph[i].append((j,flow[j]))

def Prim(graph,start):
    d[start]=0 # 첫 시작 가중치 0으로 갱신
    h=[]
    heapq.heappush(h,(0,start)) # 우선순위 큐에 시작점 입력
    while Q:
        w,u=heapq.heappop(h) # 인접 정점 중 가장 가중치가 작은 정점 반환
        if u not in Q:
            continue
        Q.remove(u)
        for i in graph[u]: # 인접 정점 순환하기
            if i[0] in Q and i[1]<d[i[0]]: # 가중치가 더 작다면
                d[i[0]]=i[1] # 가중치 갱신
                heapq.heappush(h,(i[1],i[0])) # 우선순위 큐에 입력
    return sum(d) # 최소신장트리의 모든 가중치 반환

print(Prim(graph,0))