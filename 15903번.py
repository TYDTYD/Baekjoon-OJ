import sys
import heapq
input=sys.stdin.readline

n,m=map(int,input().split()) # 카드 개수와 카드 합체 횟수 입력 받기

card=list(map(int,input().split())) # 카드 상태 입력받기

for i in range(m): # 카드 합체 횟수만큼 반복
    heapq.heapify(card)  # 배열 힙정렬
    x=heapq.heappop(card) # 배열 안에 있는 최솟값 x에 할당
    y=heapq.heappop(card) # 배열 안에 있는 최솟값 y에 할당
    heapq.heappush(card,x+y) # x+y 값 배열에 넣기
    heapq.heappush(card,x+y)

print(sum(card)) # 배열의 합 출력