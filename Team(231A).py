x = int(input())
list = 0
for i in range(x):
    y = input()
    u = y.count("1")
    if u > 1:
        list += 1
print(list)