n, m, k = map(int, input().split())  
meal = list(map(int, input().split()))  
ans = 0  
for i in meal:  
    if i == 1:  
        if m > 0:  
            m -= 1  
        else:  
            ans += 1  
    else:  
        if k > 0:  
            k -= 1  
        elif m > 0:  
            m -= 1  
        else:  
            ans += 1  

print(ans)
