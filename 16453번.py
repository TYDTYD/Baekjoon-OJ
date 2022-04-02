from collections import deque
n,m=map(int,input().split())
answer=0
k=0

q=list(map(int,input().split()))

a=deque([i+1 for i in range(n)])

q.index(a[k])
#-a[0]<len(a)-q.index(q[k])+a.index(a[0])
       
     
print(q.index(a[k]))


#h=[int(ch) for ch in input().split(' ')]


#h.sort()

#for j in range(n):
#    if l>=h[j]:
#       l=l+1

#print(l)