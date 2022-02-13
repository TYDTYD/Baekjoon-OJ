import sys
input=sys.stdin.readline

def one(x):
    ans=x&1
    for i in range(54,0,-1):
        if x&2**i:
            ans+=count[i-1]+(x-(2**i)+1)
            x-=2**i
    return ans

a,b=map(int,input().split())
count=[0]*55
count[0]=1

for i in range(1,55):
    count[i]=2*count[i-1]+2**i

answer=one(b)-one(a-1)

print(answer)