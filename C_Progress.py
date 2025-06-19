pg = int(input())
days = list(map(int, input().strip().split()))
ans = 0
while pg > 0:
    for i in range(7):
        pg -= days[i]
        if pg <= 0:
            ans = i+1
            break
print(ans)