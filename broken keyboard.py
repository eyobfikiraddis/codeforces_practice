tm = int(input())
for i in range(tm):
    string = input()
    ls = []
    for j in string:
        ls.append(j)
    x = 0
    y = 1
    res = ""
    while y <= len(ls):
        if y == len(ls) or ls[x] != ls[y]:
            res += ls[x]
            x += 1
            y += 1
        else:
            ls.pop(y)
            ls.pop(x)
    res = ''.join(sorted(res))
    print(res)


