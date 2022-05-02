import sys
input=sys.stdin.readline

def buildHeap(a,n):
    for i in range(n//2,0,-1):
        heapify(a,i,n)

def heapify(a,k,n): # a[k]를 루트로 하는 트리를 힙성질을 만족하도록 수선한다
    left=2*k
    right=2*k+1
    switch=0

    if right<=n: # k가 두 자식을 가지는 경우
        if a[left]<a[right]:
            smaller=left
        else:
            smaller=right
    elif left<=n: # k의 왼쪽 자식만 있는 경우
        smaller=left
    else: # k가 리프노드인 경우
        return 

    if a[smaller]<a[k]:
        switch=a[k]
        a[k]=a[smaller]
        a[smaller]=switch
        heapify(a,smaller,n)

def remove(a):
    result=a[1]
    a[1]=a[-1]
    a.pop()
    heapify(a,1,len(a)-1)
    return result

n=int(input())
a=[None]

for i in range(n):
    x=int(input())
    if x==0 and len(a)!=1:
        print(remove(a))
    elif x==0:
        print(0)
    else:
        a.append(x)
        buildHeap(a,len(a)-1)