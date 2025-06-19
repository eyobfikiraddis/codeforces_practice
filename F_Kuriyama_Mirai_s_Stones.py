n = int(input())
v = list(map(int, input().split()))
p = [0]* (n+1)
for i in range(n):
    p[i+1] = p[i] + v[i]
u = sorted(v)
pu = [0]* (n+1)
for i in range(n):
    pu[i+1] = pu[i] + u[i]
m = int(input())
for i in range(m):
    t,l,r = map(int, input().split())
    if t == 1:
        print(p[r] - p[l-1])
    else:
        print(pu[r] - pu[l-1])