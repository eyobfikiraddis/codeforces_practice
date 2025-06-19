c = int(input())
coins = sorted(list(map(int, input().strip().split())), reverse=True)
total = 0
for i in coins:
    total += i
ans = 0
t = 0
for i in coins:
    if t > total:
        break
    else:
        total -= i
        ans += 1
        t += i
print(ans)