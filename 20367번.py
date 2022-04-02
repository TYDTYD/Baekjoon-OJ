import sys
input=sys.stdin.readline

n=int(input())

a=list(map(int,input().split()))
a.sort()

print(a)
#비슷한 랭킹 순서끼리 하면 되지만 또 큰 수가 버려지는 것도 고려해야 한다