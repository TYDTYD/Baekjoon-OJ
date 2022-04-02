import sys
input=sys.stdin.readline


R,C,M=map(int,input().split())
graph=[list(0 for i in range(R+1)) for j in range(C+1)]
shark=[]
score=0

for i in range(M):
    r,c,s,d,z=map(int,input().split())
    graph[c][r]=(s,d,z)

for i in range(C):
