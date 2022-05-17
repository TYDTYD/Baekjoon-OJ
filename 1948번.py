from collections import deque
import sys
sys.setrecursionlimit(20000)
input=sys.stdin.readline

n=int(input())
m=int(input())

result=[0]*(n+1) # dp배열
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
graphR=[[] for _ in range(n+1)] # 역추적 그래프
visited=[[False for _ in range(n+1)] for _ in range(n+1)] # 경로마다 방문처리 배열 만들기

for i in range(1,m+1):
    p,q,r=map(int,input().split())
    indegree[q]+=1
    graph[p].append((q,r))
    graphR[q].append((p,r)) # graph와는 거꾸로 도로 저장

start,end=map(int,input().split())

q=deque()

for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    index=q.popleft()
    for i in graph[index]:
        indegree[i[0]]-=1
        result[i[0]]=max(result[i[0]],result[index]+i[1])
        if indegree[i[0]]==0:
            q.append(i[0])

def dfsR(graph,v,visited,res,count): # dfs로 경로 역추적
    for i in graph[v]:
        if not visited[v][i[0]]: # 방문하지 않은 경로라면
            visited[v][i[0]]=True # 방문처리
            res-=i[1] # 만나는 시간 - 도로 건너는데 걸리는 시간
            if res==result[i[0]]: # dp배열에 저장된 시간과 같다면
                count+=dfsR(graph,i[0],visited,res,1) # 도로 수 세기
            res+=i[1] # 다시 시간 +
    return count

print(result[end])
print(dfsR(graphR,end,visited,result[end],0))