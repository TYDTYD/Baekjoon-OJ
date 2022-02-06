import sys
import math
input=sys.stdin.readline

a,b=map(int,input().split())
count=0

for i in range(54):
    if b//2**i==0 and count==0:
        count=i
        break

print(count,2**count)