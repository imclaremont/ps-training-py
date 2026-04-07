import sys

n = int(input())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        print(stack.pop() if stack else -1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
