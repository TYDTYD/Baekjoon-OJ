import sys
input=sys.stdin.readline

n,m=map(int,input().split())
index1=[]
index2=[]

for i in range(n):
    index1.append(input())
    
for i in range(m):
    index2.append(input())

print(set(index1+index2))
