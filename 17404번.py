import sys
input=sys.stdin.readline
INF=10**12

n=int(input())
RGB=[]
DP=[[0,0,0] for i in range(n-1)]
DP[-1]=[INF,INF,INF]
index=[0,1,2]


for i in range(n):
    RGB.append([int(x) for x in input().split()])

if n==2:
    for i in range(n-1):
        DP[i][0]=min(RGB[i][0]+RGB[i-1][1],RGB[i][0]+RGB[i-1][2])
        DP[i][1]=min(RGB[i][1]+RGB[i-1][0],RGB[i][1]+RGB[i-1][2])
        DP[i][2]=min(RGB[i][2]+RGB[i-1][0],RGB[i][2]+RGB[i-1][1])
else:
    for i in range(n-1):
        if i==0:
            DP[i][0]=min((RGB[i][0]+RGB[i-1][1],1),(RGB[i][0]+RGB[i-1][2],2))
            DP[i][1]=min((RGB[i][1]+RGB[i-1][0],0),(RGB[i][1]+RGB[i-1][2],2))
            DP[i][2]=min((RGB[i][2]+RGB[i-1][0],0),(RGB[i][2]+RGB[i-1][1],1))
        elif i!=n-2:
            DP[i][0]=min((RGB[i][0]+DP[i-1][1][0],DP[i-1][1][1]),(RGB[i][0]+DP[i-1][2][0],DP[i-1][2][1]))
            DP[i][1]=min((RGB[i][1]+DP[i-1][0][0],DP[i-1][0][1]),(RGB[i][1]+DP[i-1][2][0],DP[i-1][2][1]))
            DP[i][2]=min((RGB[i][2]+DP[i-1][0][0],DP[i-1][0][1]),(RGB[i][2]+DP[i-1][1][0],DP[i-1][1][1]))
        else:
            for j in range(3):
                for k in range(3):
                    if DP[i-1][j][1]==k:
                        if j==k:
                            DP[i][j-1]=min(DP[i][j-1],RGB[i][j-1]+DP[i-1][j][0])
                            DP[i][j-2]=min(DP[i][j-2],RGB[i][j-2]+DP[i-1][j][0])
                        else:
                            for h in index:
                                if h!=j and h!=k:
                                    DP[i][h]=min(DP[i][h],RGB[i][h]+DP[i-1][j][0])
                    
print(min(DP[-1]))
print(DP)