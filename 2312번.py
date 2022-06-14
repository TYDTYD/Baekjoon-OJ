import math
import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())
    p=n
    array=[False for _ in range(n+1)]
    count=0
    index=[]

    for i in range(2,n+1):
        if array[i]==False: # i가 소수라면
            while(p%i==0): 
                p=p//i
                count+=1 # p가 i로 몇번 나뉘는지 카운트
            if count!=0:
                index.append((i,count)) # index 배열에 인수 저장
            j=2
            while i*j<=n:
                array[i*j]=True
                j+=1
        count=0

    for i in index:
        print(i[0],i[1])