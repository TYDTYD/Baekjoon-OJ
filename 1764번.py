import sys

n, m = map(int, sys.stdin.readline().split())
not_heard = [sys.stdin.readline().strip() for _ in range(n)]
never_seen = [sys.stdin.readline().strip() for _ in range(m)]

result = sorted(list(not_heard & never_seen))

print(len(result))
for i in result:
    print(i)