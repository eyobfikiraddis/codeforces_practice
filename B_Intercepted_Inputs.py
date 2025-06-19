n = int(input())
for i in range(n):
    x = int(input()) - 2
    y = list(map(int, input().split()))
    h = ""
    for j in range(len(y)):
        if h:
                    break
    
        for k in range(j+1, len(y)):
            if y[j] * y[k] == x:
                h = str(y[j]) + " " + str(y[k])
                break
    print(h)