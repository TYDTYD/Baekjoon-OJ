import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    if x>=m or x<=-1 or y>=n or y<=-1:
        return False
    if farm[x][y]==0:
        return False
    if farm[x][y]==1:
        farm[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

T=int(input())
result=0
answer=[]

for i in range(T):
    m,n,k=map(int,input().split())
    result=0
    farm=[]
    for i in range(m):
        farm.append([ 0 for j in range(n)])
    for j in range(k):
        a,b=map(int,input().split())
        for k in range(m):
            for l in range(n):
                if k==a and l==b:
                    farm[k][l]=1
    for q in range(m):
        for p in range(n):
            if dfs(q,p)==True:
                result=result+1
    answer.append(result)

for t in range(T):
    print(answer[t])