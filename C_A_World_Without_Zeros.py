a = input()
b = input()
az = a.replace("0","")
bz = b.replace("0","")
c = str(int(a) + int(b)).replace("0","")
cz = str(int(az) + int(bz)).replace("0","")
if cz == c:
    print("YES")
else:
    print("NO")