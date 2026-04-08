import sys

T = int(sys.stdin.readline())
for _ in range(T):
    str = sys.stdin.readline().strip()

    stack = []
    f = 0
    for ch in str:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                f = 1
                break

    if not stack and f == 0:
        print("YES")
    else:
        print("NO")
        
