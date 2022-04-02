import sys
input=sys.stdin.readline

n=int(input())
f=[0 for i in range(n+2)]

def fib(n):
    f[1]=1
    f[2]=1
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]

print(fib(n))