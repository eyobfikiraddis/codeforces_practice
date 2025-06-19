x = input().split()
y = input().split()
g = 0
for i in y:
    if i == " ":
        pass
    elif int(i) > int(x[-1]):
        g += 1
if g == 0:
    u = set(y)
    if len(u) == 1 and y[0] != "0":
        g = int(x[0])
        
print(g)
