n = int(input())
ls = list(map(int, input().strip().split()))
ls.sort()
mex = 1
for i in ls:
    if i >= mex:
        mex += 1
print(mex)