from collections import deque
n = int(input())


def solution():
    cmd = input()
    dec = deque()

    for i in cmd:
        if i == "(":
            dec.append("(")
        else:
            if dec:
                dec.popleft()
            else:
                print("NO")
                return

    print("NO" if dec else "YES")
    return


for i in range(n):
    solution()