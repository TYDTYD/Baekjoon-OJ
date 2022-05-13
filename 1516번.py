from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
time=[] # 각 건물 개발시간 저장하는 배열
result=[0]*(n+1) # dp 배열
indegree=[0]*(n+1) # 각 점마다 진입차수 저장하는 배열
graph=[[] for _ in range(n+1)]
q=deque()

for i in range(1,n+1):
    build=list(map(int,input().split()))
    time.append(build[0]) # build의 첫번째 원소 저장
    for j in range(1,len(build)-1): # build의 두번째 원소부터 마지막 두번째 원소까지
        graph[build[j]].append(i) # 건물 번호 저장
        indegree[i]+=1 # 진입차수 1 증가

for i in range(1,n+1):
    if indegree[i]==0: # 진입차수가 0인 곳을 q에 넣기
        q.append(i)

while q:
    index=q.popleft() # q에 마지막 원소 index에 할당
    for i in graph[index]: # index와 이어지는 건물들 순환
        indegree[i]-=1 # 진입차수 제거
        result[i]=max(result[i],result[index]+time[index-1]) # 진입차수가 여러개일 경우 모든 진입차수가 들어와야 건설이 완료되므로
        if indegree[i]==0:
            q.append(i)

for i in range(1,n+1):
    print(result[i]+time[i-1]) # i번 건물을 개발하기 위한 건물을 짓는 최대 시간 + i번 건물을 개발하는 시간