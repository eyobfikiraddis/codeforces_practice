s = input()
k = int(input())

if k > len(s):
    print("impossible")
else:
    x = set(s)
    y = max(0, k-len(x))
    print(y)