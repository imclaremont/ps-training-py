import sys

T = int(sys.stdin.readline())

res = []
for _ in range(T):
    ps = sys.stdin.readline().strip()
    
    cnt = 0
    is_vps = True

    for ch in ps:
        if ch == "(":
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            is_vps = False
            break
    
    if cnt == 0 and is_vps:
        res.append("YES")
    else:
        res.append("NO")

print("\n".join(res))
