shift = input()
typd = input()
lett = "qwertyuiopasdfghjkl;zxcvbnm,./"
x = 1 if shift == "R" else -1
ans = ""
for i in range(len(typd)):
    if typd[i] not in lett:
        ans += typd[i]
    else:
        y = lett.index(typd[i]) - x
        if y == len(lett):
            y = 0
        ans += lett[y]
print(ans)