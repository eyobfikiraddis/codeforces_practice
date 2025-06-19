n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append((a,b))
l.sort()
for i in range(n - 1):
    if l[i][1] > l[i+1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")