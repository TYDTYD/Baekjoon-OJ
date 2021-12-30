import sys
input=sys.stdin.readline

a,b=map(int,input().split())
start=[1]

for i in range(1,53):
    if b<2**(i+1):
        diff=2**(i+1)-b+1
        break
    start.append(start[i-1]+start[i-1]+2**(i-1))

print(diff,start)

result=sum(start)
index=0

while(diff>0):
    if diff>=(len(start)-index):
        result=result+2**(len(start)-index)
        diff=diff-(len(start)-index)
    else:
        index+=1
    
print(result)