x = list(map(int, input().split()))
y = list(map(int, input().split()))
n = x[0]
k = x[1]

given = 0
days = 0
while given < k:
    if days >= len(y):
        days = -1
        break
    g = 8 if y[days] > 8 else y[days]
    days += 1
    given += g
print(days)