import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

def mergeSort(a,p,r): # p-처음 부분 r-마지막 부분
    if p<r: # p와 r이 똑같아 질때까지 재귀 반복
        q=(p+r)//2
        mergeSort(a,p,q)
        mergeSort(a,q+1,r)
        merge(a,p,q,r)
    return a

def merge(a,p,q,r):
    tmp=[]
    i=p
    j=q+1
    while(i<=q and j<=r): # 각 리스트의 범위를 넘기기 전까지
        if a[i]<=a[j]: # 두 배열의 원소를 대소비교
            tmp.append(a[i]) # 임시 리스트에 삽입
            i+=1
        else:
            tmp.append(a[j]) # 임시 리스트에 삽입
            j+=1
    while(i<=q): # 왼쪽 부분 배열이 남은 경우
        tmp.append(a[i])
        i+=1
    while(j<=r): # 오른쪽 부분 배열이 남은 경우
        tmp.append(a[j])
        j+=1
    i=p
    k=0
    while(i<=r):
        a[i]=tmp[k] # 모든 정렬된 결과를 저장
        i+=1
        k+=1
    return a

mergeSort(a,0,len(a)-1)

def binary_search(x,y,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if x[mid]==y:
        return 1
    elif x[mid]>y:
        return binary_search(x,y,start,mid-1)
    elif x[mid]<y:
        return binary_search(x,y,mid+1,end)
    else:
        return 0

for i in range(m):
    print(binary_search(a,b[i],0,n-1))