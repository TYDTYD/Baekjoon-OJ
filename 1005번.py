from collections import deque
import sys
input=sys.stdin.readline

T=int(input())
answer=[]

while(T>0):
    init=[]
    T-=1
    v,e=map(int, input().split())
    time=list(map(int,input().split()))

    result=[0]*(v+1)
    indegree=[0]*(v+1)
    graph=[[] for i in range(v+1)]

    for i in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    want=int(input())

    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while(indegree[want]>0):
        index=q[0]
        q.popleft()
        for i in graph[index]:
            indegree[i]-=1
            result[i]=max(result[i],result[index]+time[index-1])
            if indegree[i]==0:
                q.append(i)
    answer.append(result[want]+time[want-1])

for i in range(len(answer)):
    print(answer[i])