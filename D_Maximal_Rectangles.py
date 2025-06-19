
t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n == 0:
        print(0)
        continue
    maxa = 0
    tot1 = s.count('1')
    if tot1 == 0:
        print(0)
        continue
    doubled = s + s
    maxcon = 0
    now = 0
    for c in doubled:
        if c == '1':
            now += 1
            maxcon = max(maxcon, now)
        else:
            now = 0
    if maxcon >= n:
        print(n * n)
    else:
        maxa = 0
        for k in range(maxcon):
            area = (k + 1) * (maxcon - k)
            if area > maxa:
                maxa = area
        print(maxa)
