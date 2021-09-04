# 1. 동전
> 정답 코드
```python
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[k])
```

<br>
<b>다이나믹 프로그래밍 문제</b>
<br> dp[i - coin]에서 구했던 경우의 수를 dp[i]에 더해주는 동적 할당
<br><br><br><br><br><br>

# 2. 촌수계산
> 정답 코드
```python
from collections import deque

def bfs(x):
    q = deque()
    q.appendleft(x)
    visit[x] = 0
    while q:
        x = q.pop()
        if x == b:
            return visit[x]
        for i in graph[x]:
            if visit[i] != 0:
                continue
            else:
                visit[i] = visit[x] + 1
                q.appendleft(i)
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visit = [0] * (n + 1)

print(bfs(a))
```

<br>
<b>그래프탐색 문제</b>
<br> 그래프를 a부터 탐색해서 b를 찾으면 그 순서를 반환한다.
<br> 그래프를 전부 돌아도 b가 나오지 않으면 두 노드가 연결되어 있지 않다고 생각하고 -1을 반환한다.
<br><br><br><br><br><br>