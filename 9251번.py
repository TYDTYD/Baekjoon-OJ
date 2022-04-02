import sys
input=sys.stdin.readline

a=input()
b=input()
C=[]

def LCS(m,n,c,d):
    for i in range(m):
        C.append([0 for j in range(n)])
    for i in range(1,m):
        for j in range(1,n):
            if c[i-1]==d[j-1]:
                C[i][j]=C[i-1][j-1]+1
            else:
                C[i][j]=max(C[i-1][j],C[i][j-1])
    return C[m-1][n-1]

if len(a)<len(b):
    print(LCS(len(a),len(b),a,b))
else:
    print(LCS(len(b),len(a),b,a))