import sys
from collections import deque
# 입력 속도
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    commands = input().split()

    if commands[0] == 'push': # push X: 정수 X를 큐에 넣는 연산이다.
        q.append(commands[1])
    elif commands[0] == 'pop': # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(q) == 0:
            print(-1)
        else: # popleft()는 효율적으로 큐의 가장 앞에 있는 요소를 제거하고 반환하는 메서드입니다.
            # 일반적으로 큐에서 요소를 제거할 때는 pop(0)을 사용하지만, 이는 리스트의 모든 요소를 이동시키기 때문에 비효율적입니다. 
            # 반면에 popleft()는 O(1)의 시간 복잡도로 요소를 제거할 수 있습니다.
            print(q.popleft())
    elif commands[0] == 'size': # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(q))
    elif commands[0] == 'empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == 'front': # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif commands[0] == 'back': # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(q) == 0:
            print(-1)
        else: 
            print(q[-1])
