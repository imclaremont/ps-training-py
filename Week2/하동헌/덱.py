import sys
from collections import deque

N = int(sys.stdin.readline())

deque = deque()
res = []
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        deque.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        deque.append(cmd[1])
    elif cmd[0] == "pop_front":
        if deque:
            res.append(deque.popleft())
        else:
            res.append("-1")
    elif cmd[0] == "pop_back":
        if deque:
            res.append(deque.pop());
        else:
            res.append("-1")
    elif cmd[0] == "size":
        res.append(str(len(deque))) # 마지막 출력 join() 함수 때문에 int를 문자열로 치환해줘야 한다 (참고로 데크 안의 모든 변수 자료형을 통일시켜야 되는 건 아님, 파이썬은 동적 언어라)
    elif cmd[0] == "empty":
        if deque:
            res.append("0")
        else:
            res.append("1")
    elif cmd[0] == "front":
        if deque:
            res.append(deque[0])
        else:
            res.append("-1")
    elif cmd[0] == "back":
        if deque:
            res.append(deque[-1])
        else:
            res.append("-1")

print("\n".join(res))
