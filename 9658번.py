import sys
input=sys.stdin.readline

n=int(input())
n1=n
b=0
while(n1>0):
    n1=n1//4
    b=b+1

win=[]
lose=[]
a=0

while(a<=100):
    for i in range(1,b):
        if a<1:
            lose.append(a)
        elif a-1 in lose:
            win.append(a)
        elif a-(4**i) in lose:
            win.append(a)
        elif a-1 in win:
            lose.append(a)
        elif a-(4**i) in win:
            lose.append(a)
        a=a+1

print(win,lose)
if n in win:
    print("SK")
else:
    print("CY")