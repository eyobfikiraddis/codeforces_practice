n = int(input())  
current_day = 0  

for _ in range(n):  
    s, d = map(int, input().split())  

    if s >= current_day:  
        current_day = s  
    else:  
        k = (current_day - s + d - 1) // d  
        current_day = s + k * d  

    current_day += 1  

print(current_day - 1)
