import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
# 이차원 배열로 방문처리 해야됨 각 간선을 거쳤는지 일일이 다 확인해야 하는 미친 문제
def dfs(graph,v,visited,count,index):
    if count!=0:
        visited[v]=True
    if count==4:
        return True
    for i in graph[v]:
        if not visited[i]:
            if i==index:
                dfs(graph,i,visited,count,index)
            elif dfs(graph,i,visited,count+1,index):
                return True
    return False

n,m=map(int,input().split())
graph=[ [] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited=[False]*n
    if dfs(graph,i,visited,0,i):
        print(1)
        exit(0)

print(0)