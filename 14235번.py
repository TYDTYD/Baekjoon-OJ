import sys
import heapq
input=sys.stdin.readline

n=int(input()) # 방문한 횟수 입력
gift=[]

for i in range(n): # 횟수만큼 반복
    gifts=list(map(int,input().split())) 
    if gifts[0]==0: # 0이라면
        if len(gift)==0:
            print(-1)
        else:
            print(-(heapq.heappop(gift))) # 배열 안에 가장 큰 원소 반환
    else: # 0이 아니라면
        for i in range(gifts[0]): # 배열 첫번째 원소만큼 반복
            heapq.heappush(gift,-gifts[i+1]) # 배열 두번째 원소부터 최대값 반환을 위해 -값 삽입