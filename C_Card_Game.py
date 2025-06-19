n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))
num = list(set(nums))
if nums.count(num[0]) == n//2 and nums.count(num[1]) == n//2:
    print("YES")
    for i in num:
        if i != nums[0]:
            r = i
    print(str(nums[0])+ " " + str(r))
else:
    print("NO")