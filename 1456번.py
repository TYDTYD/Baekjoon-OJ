import math
import sys
input=sys.stdin.readline

count=0
a,b=map(int,input().split())

array=[True for _ in range(int(math.sqrt(b)+1))] # 루트 b까지의 True 배열

for i in range(2,int(math.sqrt(b)+1)):
    if array[i]==True:
        j=2
        while(int(math.sqrt(b)+1)>i*j):
            array[i*j]=False
            j+=1
        j=2
        while(b>=i**j): # b보다 작거나 같고
            if a<=i**j: # a보다 크거나 같은 소수의 n제곱이라면
                count+=1 # count 1 증가
            j+=1

print(count)