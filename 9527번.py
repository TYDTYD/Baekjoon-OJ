import sys
input=sys.stdin.readline

a,b=map(int,input().split())

first=[0,1,1,2]
dp=[0,0,0,0]
count=2
idx=0
asum=0

for i in range(b+1):
    dp[i%4]+=first[i]
    first.append(first[idx%2**count]+1)
    idx+=1
    if idx%2**count==0:
        idx=0
        count+=1
    if a==i+1:
        asum=sum(dp)

print(sum(dp)-asum)