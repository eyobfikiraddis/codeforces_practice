l, r, x, y, k = map(int, input().split())
flag = 1
for b in range(x, y+1):
    if b*k >= l and b*k <= r:
        print("YES")
        flag = 0
        break
if flag == 1:
    print("NO")