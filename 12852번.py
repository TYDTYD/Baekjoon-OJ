n=int(input())

dp=[(0,0)]*(n+1)
index=[n]

for i in range(2,n+1):
    if i%6==0:
        dp[i]=min((dp[i//3][0]+1,1),(dp[i//2][0]+1,2),(dp[i-1][0]+1,3))
    elif i%3==0:
        dp[i]=min((dp[i//3][0]+1,1),(dp[i-1][0]+1,3))
    elif i%2==0:
        dp[i]=min((dp[i//2][0]+1,2),(dp[i-1][0]+1,3))
    else:
        dp[i]=(dp[i-1][0]+1,3)

a=n
while(a!=1):
    if dp[a][1]==1:
        a=a//3
        index.append(a)
    elif dp[a][1]==2:
        a=a//2
        index.append(a)
    else:
        a=a-1
        index.append(a)

print(dp[n][0])
for i in index:
    print(i,end=' ')