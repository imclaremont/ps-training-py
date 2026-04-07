from collections import deque
n, k = map(int, input().split())

dec = [i for i in range(1, n + 1)]
answer = []
idx = 0
while dec:
    for _ in range(k - 1):
        idx += 1
        if idx >= len(dec):
            idx = 0
    answer.append(dec.pop(idx))
    if idx >= len(dec):
        idx = 0





print("<" + ", ".join(map(str, answer)) + ">")






