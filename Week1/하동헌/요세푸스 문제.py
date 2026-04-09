import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque(range(1, N + 1))

result = []
while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<" + ", ".join(result) + ">")
