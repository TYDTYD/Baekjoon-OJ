import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+30)
dp[0]=1
tile=[2,2,2]

for i in range(3,n+1):
    if i%2==0:
        tile.append(i)
        tile.append(i)

for i in range(n):
    for j in tile:
        dp[i+j]=dp[i+j]+dp[i]

<<<<<<< HEAD
print(dp)
=======
print(dp[n])
>>>>>>> 82e4a7a29d8522e6baf766167445420e72546b25
