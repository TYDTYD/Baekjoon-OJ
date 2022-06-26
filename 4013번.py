import sys
sys.setrecursionlimit(10**6)
from collections import deque
input=sys.stdin.readline

def DFS(v,visited,stack): # dfs 탐색
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            DFS(i,visited,stack)
    stack.append(v) # 방문 순서대로 스택에 넣기

def DFSR(v,visited,stack): # 역 dfs 탐색
    visited[v]=True
    stack.append(v)
    index[v]=idx # v의 대표원소를 idx로 설정 ( 최소신장트리=>크루스칼 알고리즘에도 비슷한 개념이 적용됨 )
    for i in graphR[v]:
        if not visited[i]:
            DFSR(i,visited,stack)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
graphR=[[] for _ in range(n+1)]
visited=[False]*(n+1)
stack=[]
index=[-1]*(n+1)
atm=[-1]*(n+1)
checked=[False]*(n+1)
idx=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graphR[b].append(a)

for i in range(1,n+1):
    cash=int(input())
    atm[i]=cash

s,p=map(int,input().split())
restaurant=list(map(int,input().split()))

for i in restaurant: # 레스토랑 있는 위치를 배열로 체크하기
    checked[i]=True # 레스로랑이 있으므로 체크

for i in range(1,n+1): # dfs 탐색
    if not visited[i]:
        DFS(i,visited,stack)

visited=[False]*(n+1)
SCC=[] # scc들을 모아놓기 위한 배열
scc_sum=[] # 같은 scc 원소의 현금의 합
idx=0 # scc의 개수

while stack: # 스택이 빌때까지
    scc=[]
    scc_plus=0
    point=stack.pop()
    if not visited[point]:
        DFSR(point,visited,scc)
        SCC.append(scc) # SCC 배열에 하나의 scc 그룹을 넣기
        for i in scc:
            scc_plus+=atm[i] # scc 하나의 그룹에 있는 위치의 atm 현금들을 모두 합하기
        scc_sum.append(scc_plus) # scc_sum 배열에 scc 그룹의 현금의 합 넣기
        idx+=1

start=-1 # scc 관점의 시작지점

for i in range(idx):
    if s in SCC[i]: # SCC배열에 시작지점이 있다면
        start=i # start에 scc 배열의 인덱스 넣기
        break

scc_indegree=[0]*idx # scc 그래프 상의 진입간선
scc_graph=[[] for _ in range(idx)] # scc 그래프
scc_checked=[False]*idx # scc 방문체크 그래프

for i in range(1,n+1):
    for j in graph[i]:
        if index[i]!=index[j]: # i와 j가 서로 다른 scc 라면 ( i와 j의 대표원소가 다르다면 )
            scc_graph[index[i]].append(index[j]) # scc 그래프[i]에 j의 대표원소 넣기 
    if checked[i]: # 만약 레스토랑이 있는 곳이라면
        scc_checked[index[i]]=True # i가 속한 scc를 방문 처리 (scc 방문체크 배열의 i의 대표원소를 방문 처리)

visited=[False]*(idx)

def dfs(v): # 시작지점으로부터 도달할 수 있는 지점을 확인하기 위한 dfs
    visited[v]=True
    for i in scc_graph[v]:
        scc_indegree[i]+=1 # 도달 가능한 곳만 진입간선 처리
        if not visited[i]:
            dfs(i)

dfs(start) # 시작지점부터 dfs 돌리기

q=deque()
DP=[0]*idx
DP[start]=scc_sum[start] # DP 첫 시작 지점에 start가 속한 scc의 현금의 합 넣기

q.append(start)

while q: # 위상정렬 시작
    c=q.popleft()
    for i in scc_graph[c]:
        scc_indegree[i]-=1
        DP[i]=max(DP[i],DP[c]+scc_sum[i]) # DP 점화식
        if scc_indegree[i]==0:
            q.append(i)

answer=0

for i in range(idx):
    if scc_checked[i]: # 레스토랑이 있는 scc라면
        answer=max(answer,DP[i]) # answer 갱신

print(answer)