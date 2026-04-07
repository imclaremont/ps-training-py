import sys
from collections import deque
n = int(input())
queue = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)


