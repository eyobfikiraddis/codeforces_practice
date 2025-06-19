n = int(input())  
a = list(map(int, input().split()))  
a.sort()
flag = 1
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        print("YES")
        flag = 0
        break
if flag == 1:
    print("NO")