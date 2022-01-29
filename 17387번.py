import sys
sys.stdin.readline

x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

if x1==x2 and x3==x4: # x축과 평행할 때
    if x1==x3:
        if min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
            print(1)
        else:
            print(0)
    else:
        print(0)
elif y1==y2 and y3==y4: # y축과 평행할 때
    if y1==y3:
        if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2):
            print(1)
        else:
            print(0)
    else:
        print(0)
elif x1==x2: # 한 선분만 x축과 평행할 때
    m2=(y4-y3)/(x4-x3)
    dx=x1
    dy=m2*(dx-x3)+y3
    if dy<=y3 and dy>=y4 or dy>=y3 and dy<=y4:
        print(1)
    else:
        print(0)
elif x3==x4:
    m1=(y2-y1)/(x2-x1)
    dx=x3
    dy=m1*(dx-x1)+y1
    if dy<=y1 and dy>=y2 or dy>=y1 and dy<=y2:
        print(1)
    else:
        print(0)
elif y1==y2: # 한 선분만 y축과 평행할 때
    m2=(y4-y3)/(x4-x3)
    dy=y1
    dx=(dy-y3)/m2+x3
    if dx<=x3 and dx>=x4 or dx>=x3 and dx<=x4:
        print(1)
        print(dx)
    else:
        print(0)
elif y3==y4:
    m1=(y2-y1)/(x2-x1)
    dy=y3
    dx=(dy-y1)/m1+x1
    if dx<=x1 and dx>=x2 or dx>=x1 and dx<=x2:
        print(1)
    else:
        print(0)
else:
    m1=(y2-y1)/(x2-x1)
    m2=(y4-y3)/(x4-x3)
    if m1==m2: # 기울기가 같을 때
        if y1-m1*x1==y3-m2*x3:
            if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2):
                print(1)
            else:
                print(0)
        else:
            print(0)
    else: # 기울기가 같지 않을 때
        dx=((m1*x1)-(m2*x3)+y3-y1)/(m1-m2)
        dy=m1*(dx-x1)+y1
        if dx>=x1 and dx<=x2 and dy>=y1 and dy<=y2 or dx>=x1 and dx<=x2 and dy<=y1 and dy>=y2 or dx>=x1 and dx<=x2 and dy<=y1 and dy>=y2 or dx<=x1 and dx>=x2 and dy<=y1 and dy>=y2:
            if dx>=x3 and dx<=x4 and dy>=y3 and dy<=y4 or dx>=x3 and dx<=x4 and dy<=y3 and dy>=y4 or dx>=x3 and dx<=x4 and dy<=y3 and dy>=y4 or dx<=x3 and dx>=x4 and dy<=y3 and dy>=y4:
                print(1)
            else:
                print(0)
        else:
            print(0)