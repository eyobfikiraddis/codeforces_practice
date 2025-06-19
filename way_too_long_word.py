t = int(input())
for i in range(t):
    x = input()
    if len(x) > 10:
        y = len(x) - 2
        x = f"{x[0]}{y}{x[-1]}"
    print(x)
    
    