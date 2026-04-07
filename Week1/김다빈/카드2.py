from collections import deque

n = int(input())
cards = deque(i for i in range(n, 0, -1))

while len(cards) > 1:
    cards.pop()
    tmp = cards.pop()
    cards.appendleft(tmp)


print(cards[-1])
