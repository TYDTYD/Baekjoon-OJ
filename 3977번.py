import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(v,visited,stack):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i,visited,stack)
    stack.append(v)

def dfsR(v,visited,stack):
    visited[v]=True
    index[v]=idx
    stack.append(v)
    for i in graphR[v]:
        if not visited[i]:
            dfsR(i,visited,stack)

T=int(input())

while(T):
    line=input() # 정말로 이해가 안가는 출력 형식
    if line=='\n': # 정말 이해 안되는 문제 출력 형식
        continue
    n,m=map(int,line.split())
    graph=[[] for _ in range(n)]
    graphR=[[] for _ in range(n)]
    visited=[False]*n
    stack=[]

    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graphR[b].append(a)

    for i in range(n):
        if not visited[i]:
            dfs(i,visited,stack)
        
    visited=[False]*n
    answer=[]
    idx=0
    index=[-1]*n

    while stack:
        scc=[]
        point=stack.pop()
        if not visited[point]:
            dfsR(point,visited,scc)
            idx+=1
            answer.append(sorted(scc))

    scc_indegree=[0]*idx

    for i in range(n):
        for j in graph[i]:
            if index[i]!=index[j]:
                scc_indegree[index[j]]+=1

    count=0
    scc_index=0
    
    for i in range(len(scc_indegree)):
        if scc_indegree[i]==0: # scc 그래프 상에 진입간선이 없다면 카운트
            scc_index=i 
            count+=1 
        if count>=2:
            break
    
    if count==1: # 진입간선이 0인 scc가 하나만 있다면
        for i in answer[scc_index]: # scc의 원소 출력
            print(i)
    else:
        print("Confused") # 아니라면 Confused 출력
    print()
    T-=1