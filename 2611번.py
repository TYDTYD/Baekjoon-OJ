from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

result=[0]*(n+1) # dp 배열
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
end=[0]*(n+1) # 1과 연결된 지점 찾기 위한 배열
route=[[] for _ in range(n+1)] # 경로 찾기 위한 배열
answer=[0]*(n+1)

for i in range(1,m+1):
    p,q,r=map(int,input().split())
    if q==1:
        end[p]=r # 1과 연결되어 있을 경우 end 배열에 저장(순환 방지)
    else:
        indegree[q]+=1
        graph[p].append((q,r))

q=deque()

for i in range(1,n+1):
    if i==1:
        route[i].append(1) # 출발점 1에 1 저장
    if indegree[i]==0:
        q.append(i)

while q:
    index=q.popleft()
    for i in graph[index]:
        indegree[i[0]]-=1
        if result[i[0]]<=result[index]+i[1]: # i[0]번 지점이 더 큰 점수로 갱신 되었을 경우
            route[i[0]]=[] # i[0]번 경로 초기화
            route[i[0]].extend(route[index]) # 진입 지점의 경로 그대로 저장
            route[i[0]].append(i[0]) # 본인 지점 추가
        result[i[0]]=max(result[i[0]],result[index]+i[1])
        
        if indegree[i[0]]==0:
            q.append(i[0])

for i in range(1,n+1):
    if end[i]!=0: # 1과 이어져있는 지점이라면
        answer[i]=result[i]+end[i] # answer 배열에 점수 할당

print(max(answer))
for i in route[answer.index(max(answer))]: # answer 배열중 가장 큰 점수에 있는 지점의 경로 출력
    print(i,end=' ')
print(1) # 마지막 1번 지점 출력