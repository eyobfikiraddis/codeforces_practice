tm = int(input())
for i in range(tm):
    num_of_boxes = input()
    lists = input().split()
    candies = []
    for j in lists:
        candies.append(int(j2))
    mincan = min(candies)
    to_be_eatten = 0
    for k in candies:
        to_be_eatten += k - mincan
    print(to_be_eatten)
