# 1. 좋은 단어
> 1차시도
```python
n = int(input())
words = []
for _ in range(n):
    words.append(input())

cnt = 0
for i in range(n):
    stack = []
    check = True
    for j in words[i]:
        if stack == []:
            stack.append(j)
        elif j == 'A' and stack[-1] == 'A':
            stack.pop()
        elif j == 'B' and stack[-1] == 'B':
            stack.pop()
        elif len(stack) == 1:
            stack.append(j)
        else:
            check = False
            break
    if stack != []:
        check = False
    if check:
        cnt += 1
print(cnt)
```
<br>
<b>틀린이유 : 조건을 빼먹은 것 같은데 뭘 빼먹었는지 잘 모르겠다...</b>
<br><br><br><br><br><br>

> 정답 코드
```python
n = int(input())
words = []
for _ in range(n):
    words.append(input())

cnt = 0
for i in range(n):
    stack = []
    check = True
    for j in words[i]:
        if stack == []:
            stack.append(j)
        elif stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)
    if not(stack):
        cnt += 1
print(cnt)
```

<br>
<b>빼먹은 조건을 찾을 수 없어서 단어의 문자와 스택의 문자가 같으면 pop하고 다르면 push하여 마지막에 스택이 비어있으면 True이고 스택이 비어 있지 않다면 False 이다.</b>
<br><br><br><br><br><br>

# 2. 회전하는 큐
> 정답코드
```python
from collections import deque

def left():
    x = q.popleft()
    q.append(x)
    return

def right():
    x = q.pop()
    q.appendleft(x)
    return

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
q = deque()
for i in range(1, n + 1):
    q.append(i)

cnt = 0
for i in numbers:
    if q.index(i) > len(q) // 2:
        while q[0] != i:
            right()
            cnt += 1
        q.popleft()
    else:
        while q[0] != i:
            left()
            cnt += 1
        q.popleft()

print(cnt)
```
<br>
<b>원형큐를 구현하고 left를 해야되는지 right를 해야되는지 구분하면 쉽게 해결 가능한 문제</b>
<br><br><br><br><br><br>

# 3. 나무 자르기
> 정답코드
```python
n = int(input())
trees = list(map(int, input().split()))
grow = list(map(int, input().split()))

ans = sum(trees)
grow.sort()
for i in range(n):
    ans += i * grow[i]
print(ans)
```
<br>
<b>처음에는 자라는 길이와 나무를 매치해서 먼저 잘라야 하는 나무를 골라야된다고 생각했지만<br>
어떤 나무를 먼저 자르는것은 중요하지 않고 얼마나 자라는 지가 중요했다.</b>
<br><br><br><br><br><br>

# 4. 오셀로 재배치
> 정답코드
```python
t = int(input())
for _ in range(t):
    n = int(input())
    bw1 = input()
    bw2 = input()
    cnt = 0
    b = 0
    w = 0
    for i in range(n):
        if bw1[i] != bw2[i]:
            if bw1[i] == 'B':
                b += 1
                cnt += 1
            else:
                w += 1
                cnt += 1
    print(cnt - min(b, w))
```
<br>
<b>검정돌과 흰돌 한쌍을 뒤집어야 되면 서로 바꿔주는 것으로 cnt에서 빼준다</b>
<br><br><br><br><br><br>