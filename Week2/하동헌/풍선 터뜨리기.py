# 파이썬 ps 에서는 구조가 단순할 때 굳이 딕셔너리를 안 쓰고, 튜플을 사용한다
import sys
from collections import deque

N = int(sys.stdin.readline())

papers = list(map(int, sys.stdin.readline().split()))
balloons = deque()

for i in range(N):
    balloons.append((i + 1, papers[i])) # 데크에 튜플 자료형을 저장

res = []
while balloons:
    idx, move = balloons.popleft()
    res.append(str(idx))

    if not balloons:
        break

    if move > 0:
        for _ in range(move - 1):
            balloons.append(balloons.popleft())
    else:
        for _ in range(-move):
            balloons.appendleft(balloons.pop())

print(" ".join(res))
