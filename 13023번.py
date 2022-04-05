import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
<<<<<<< HEAD
# 이차원 배열로 방문처리 해야됨 각 간선을 거쳤는지 일일이 다 확인해야 하는 미친 문제
def dfs(graph,v,visited,count,index):
    if count!=0:
        visited[v]=True
=======

def dfs(graph,v,visited,count):
    visited[v]=True
>>>>>>> 82e4a7a29d8522e6baf766167445420e72546b25
    if count==4:
        return True
    for i in graph[v]:
        if not visited[i]:
<<<<<<< HEAD
            if i==index:
                dfs(graph,i,visited,count,index)
            elif dfs(graph,i,visited,count+1,index):
                return True
=======
            if dfs(graph,i,visited,count+1):
                return True
            visited[i]=False # 거슬러 올라갈때 지나갔던 경로를 다시 미방문 처리
>>>>>>> 82e4a7a29d8522e6baf766167445420e72546b25
    return False

n,m=map(int,input().split())
graph=[ [] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited=[False]*n
<<<<<<< HEAD
    if dfs(graph,i,visited,0,i):
=======
    if dfs(graph,i,visited,0):
>>>>>>> 82e4a7a29d8522e6baf766167445420e72546b25
        print(1)
        exit(0)

print(0)