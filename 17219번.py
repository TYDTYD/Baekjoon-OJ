import sys
input=sys.stdin.readline

n,m=map(int,input().split())
index=[]
dict={}

for i in range(n):
    address,password=map(str,input().split())
    dict.update({address:password})

for i in range(m):
    index=input().split()
    print(dict.get(index[0]))