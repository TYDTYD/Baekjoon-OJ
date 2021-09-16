# 1. 최단경로
> 정답 코드
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
distance = [INF] * (v + 1)

dijkstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```

<br>
<b>다익스트라 알고리즘</b>
<br>
<img src = "https://github.com/cute700/HNU_Algorithm_Study/blob/master/sungmin/6week/img/dijkstra.png?raw=true"><br>
우선순위 큐를 이용해서 cost가 적은 노드부터 탐색해서 시간복잡도를 단축한다.
<br><br><br><br><br><br>

# 2. 시리얼 번호
> 정답 코드
```python
n = int(input())

def sumNum(x):
    ans = 0
    for i in x:
        if i.isdigit():
            ans += int(i)
    return ans

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sumNum(x), x))
for i in arr:
    print(i)
```

<br>
<b>정렬</b>
<br>
sort의 key를 이용하여 정렬하는 순서를 지정해준다.
<br>정수를 모두 합하는 것은 따로 함수를 만들어 주어야 한다.
<br><br><br><br><br><br>

# 3. 이친수
> 정답 코드
```python
n = int(input())
dp = [0] * (n + 1)
if n == 1:
    dp.append(1)
dp[1], dp[2] = 1, 1
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
```

<br>
<b>다이나믹 프로그래밍</b>
<br> dp[n] = dp[n-1] + dp[n-2] 라는 규칙성이 있다.
<br><br><br><br><br><br>

# 4. 트리의 부모 찾기
> 정답 코드
```python
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.appendleft(x)
    pNode[x] = 1
    while q:
        x = q.pop()
        for i in graph[x]:
            if pNode[i] == 0:
                pNode[i] = x
                q.appendleft(i)
    return

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

pNode = [0] * (n + 1)
bfs(1)
for i in range(2, n + 1):
    print(pNode[i])
```

<br>
<b>bfs 알고리즘</b>
<br> bfs 알고리즘으로 루트노드부터 탐색 시작한다.
<br> 바로 이전에 탐색했던 노드를 부모노드로 기록한다.
<br><br><br><br><br><br>