t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    x = p[-1] #im trying to start from the last day
    for j in range(n-2, -1, -1):
        if p[j] > x:
            ans += 1
        else:
            x = p[j]
    print(ans)
