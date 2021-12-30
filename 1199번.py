import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

def dfs(graph,x):
    for i in range(n):
        if graph[x][i]>0:
            graph[x][i]=graph[x][i]-1
            graph[i][x]=graph[i][x]-1
            dfs(graph,i)
    print(x+1,end=' ')

n=int(input())

graph=[]
idx=0

for i in range(n):
    graph.append([int(x) for x in input().split()])
    cnt=0
    for j in range(n):
        if graph[i][j]!=0:
            cnt=cnt+graph[i][j]
    if cnt%2!=0:
        idx=-1

if idx!=-1:
    dfs(graph,0)
else:
    print(-1)