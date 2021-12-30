from itertools import combinations

n,m=map(int,input().split())
c=[]

for i in range(n):
    c.append(i)

answer=list(combinations(c,m))

for i in answer:
    print(i,end=' ')