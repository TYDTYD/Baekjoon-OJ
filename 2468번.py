import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y,line):
    if x>=n or x<=-1 or y>=n or y<=-1:
        return False
    if graph[x][y]<=line:
        return False
    if graph[x][y]>line and visited[x][y]==False:
        visited[x][y]=True
        dfs(x-1,y,line)
        dfs(x+1,y,line)
        dfs(x,y-1,line)
        dfs(x,y+1,line)
        return True
    return False

n=int(input())
graph=[ [] for _ in range(n)]
area=[]
line=0

for i in range(n):
    graph[i]=list(map(int,input().split()))
    if line<max(graph[i]):
        line=max(graph[i])

for i in range(line):
    result=0
    visited=[ [False for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if dfs(a,b,i):
                result=result+1
    area.append(result)

print(max(area))