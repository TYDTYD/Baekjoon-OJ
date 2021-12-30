import sys
import heapq
input=sys.stdin.readline

n=int(input())
c=[]

for i in range(n):
    heapq.heappush(c,int(input()))

result=heapq.heappop(c)+heapq.heappop(c)

if n>2:
    n=n-2
    while(n!=0):
        n=n-1
        result=result+heapq.heappop(c)

print(result)