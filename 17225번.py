import sys
input=sys.stdin.readline
# 포장 가능 시간이란 포장을 가장 빨리 시작할 수 있는 시간
a,b,n=map(int,input().split())
store=[]
indexB=0 # 현재 상민의 포장 가능 시간을 저장할 값
indexR=0 # 현재 지수의 포장 가능 시간을 저장할 값
idx=0
count=1
result1=[]
result2=[]

for i in range(n):
    t,c,m=map(str,input().split())
    if c=='B':
        if indexB<=int(t): # 포장 가능시간보다 주문시간이 더 느리다면
            indexB=int(t) # 포장 가능시간을 주문시간으로 저장
        for j in range(int(m)): # 선물 개수만큼 반복
            store.append((indexB,1)) # 포장 시작 시간과 인덱스 1 저장
            indexB+=a # 상민이의 포장 소요시간만큼 포장 가능시간에 더하기
    else:
        if indexR<=int(t): 
            indexR=int(t)
        for j in range(int(m)):
            store.append((indexR,2)) # 포장 시작 시간과 인덱스 2 저장
            indexR+=b # 지수의 포장 소요시간만큼 포장 가능시간에 더하기

store.sort(key=lambda x:(x[0],x[1])) # 지수와 상민의 각 주문 포장 시간 정렬
# x[0] 기준으로 먼저 정렬, 그다음 x[1] 기준으로 정렬
# 상민이가 1 지수가 2이므로 상민이가 먼저 우선순위가 옴

for i in store:
    if i[1]==1: # 상민이 담당한 주문이라면
        result1.append(count) # 카운트 값 저장
        count+=1
    else: # 지수가 담당한 주문이라면
        result2.append(count) # 카운트 값 저장
        count+=1

print(len(result1))
for i in result1:
    print(i,end=' ')
print()
print(len(result2))
for i in result2:
    print(i,end=' ')