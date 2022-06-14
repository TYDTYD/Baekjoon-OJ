import math
import sys
input=sys.stdin.readline

count=0
n=int(input())
k=int(input())

if n<=k:
    print(n) # n이 k보다 크지 않다면 n 출력
else:
    array=[False for _ in range(n+1)]

    for i in range(2,int(math.sqrt(n)+1)):
        if array[i]==False:
            j=2
            while(n>=i*j):
                if not array[i*j] and (array[i] or i<=k) and (array[j] or j<=k):
                    array[i*j]=True
                j+=1

    for i in range(1,k+1): # k까지 True 처리
        array[i]=True

    for i in range(1,n+1): # n까지 True인 원소 세기
        if array[i]:
            count+=1

    print(count)