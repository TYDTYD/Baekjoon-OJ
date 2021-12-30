import sys
sys.setrecursionlimit(100000)

def dfs(x,y,visited):
    cnt=[0]
    if x>=R or x<=-1 or y>=C or y<=-1:
        return False
    if visited[ord(board[x][y])-65] is True:
        return False
    elif visited[ord(board[x][y])-65] is not True:
        visited[ord(board[x][y])-65]=True
        cnt=cnt+dfs(x-1,y,visited)
        cnt=cnt+dfs(x+1,y,visited)
        cnt=cnt+dfs(x,y-1,visited)
        cnt=cnt+dfs(x,y+1,visited)
        print(board[x][y])
    return cnt+1


R,C=map(int,input().split())

visited=[False]*26
result=0
board=[]
for i in range(R):
    board.append(input())

print(dfs(0,0,visited))