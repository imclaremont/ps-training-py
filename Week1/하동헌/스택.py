import sys

N = int(sys.stdin.readline())

stack = []
result = []
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.append(cmd[1])

    elif cmd[0] == "pop":
        if stack:
            result.append(stack.pop())
        else:
            result.append("-1")

    elif cmd[0] == "size":
        result.append(str(len(stack)))

    elif cmd[0] == "empty":
        if stack:
            result.append("0")
        else:
            result.append("1")

    elif cmd[0] == "top":
        if stack:
            result.append(stack[-1])
        else:
            result.append("-1")

print("\n".join(result))
