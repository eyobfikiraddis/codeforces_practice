n = int(input())
for i in range(n):
    s, t = input().split()
    #let me try using two pointers one for each word
    i = 0
    j = 0
    while i <len(s) and j < len(t):
        if s[i] == t[j]:
            j+= 1
        i+= 1
    if j == len(t):
        print("YES")
    else:
        print("NO")
