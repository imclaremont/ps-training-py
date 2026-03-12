import sys
from collections import deque

N = int(input())

queue = deque()
result = []
for _ in range(N):
    # N의 값이 크기 때문에 반복문 O(N)동안 input() 으로 입력받으면 시간초과가 난다
    cmd = sys.stdin.readline().split() 

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if queue:
            result.append(queue.popleft())
        else:
            result.append('-1')
    elif cmd[0] == "size":
        result.append(str(len(queue)))
    elif cmd[0] == "empty":
        if queue:
            result.append('0')
        else:
            result.append('1')
    elif cmd[0] == "front":
        if queue:
            result.append(queue[0])
        else:
            result.append('-1')
    elif cmd[0] == "back":
        if queue:
            result.append(queue[-1])
        else:
            result.append('-1')

print("\n".join(result))
