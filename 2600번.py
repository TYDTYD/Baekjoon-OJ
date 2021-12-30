import sys
input=sys.stdin.readline

b=[int(ch) for ch in input().split(' ')]
answer=[]

for i in range(5):
    k1,k2=map(int,input().split())
    answer.append(k1^k2)

print(answer)