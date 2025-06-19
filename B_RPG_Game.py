x = list(map(int, input().split()))
s = x[0]
n = x[1]  

dragons = []
for i in range(n):
    xi, yi = map(int, input().split())
    dragons.append((xi, yi))

dragons.sort()
for xi, yi in dragons:
    if s <= xi:
        print("NO")
        exit()
    s += yi
print("YES")
