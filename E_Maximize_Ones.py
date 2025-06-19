n = int(input())
a = list(map(int, input().split()))

t1 = sum(a)
maxG = 0
now = 0
for i in range(n):
    if a[i] == 0:
        now += 1
    else:
        now -= 1
    if now < 0:
        now = 0
    maxG = max(maxG, now)

if t1 == n:
    print(n - 1)
else:
    print(t1 + maxG)
