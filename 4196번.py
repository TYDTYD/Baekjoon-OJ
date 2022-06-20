import sys
sys.setrecursionlimit(500000)
input=sys.stdin.readline

def SCC(start):
    parent=start
    visited[start]=start
    stack.append(start)
    for i in node[start]:
        if not visited[i]:
            parent=min(parent,SCC(i))
        elif not finished[i]:
            parent=min(parent,visited[i])
    if parent==visited[start]:
        v=[]
        while(True):
            n=stack.pop()
            finished[n]=True
            v.append(n)
            scc[n]=parent
            if n==parent:
                break
        result_SCC.append(v)

    return parent

T=int(input())

for i in range(T):
    n,m=map(int,input().split())
    visited=[0]*(n+1)
    finished=[False]*(n+1)
    stack=[]
    count=0
    node=[[] for _ in range(n+1)]
    result_SCC=[]
    scc=[0]*(n+1)
    indegree=[0]*(n+1)

    for j in range(m):
        x,y=map(int,input().split())
        node[x].append(y)

    for i in range(1,n+1):
        if not visited[i]:
            SCC(i)

    for i in range(1,n+1):
        for j in node[i]:
            if scc[j]!=scc[i]: # i->j로 향하는 간선에서 i의 scc와 j의 scc가 다를 경우
                indegree[scc[j]]+=1 # 다른 scc집합에서 들어오는 간선 카운트

    flag=[False]*(len(result_SCC))

    for i in range(len(result_SCC)):
        for j in result_SCC[i]:
            if not flag[i]:
                if indegree[scc[j]]!=0: # scc 집합에서 다른 집합으로 들어오는 간선 카운트가 있다면
                    count+=1
                    flag[i]=True # 그 집합은 카운트에서 제외

    print(len(result_SCC)-count) # 전체 scc 집합 수 - 진입 간선이 있는 scc 집합의 수 