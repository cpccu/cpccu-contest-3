def can_make_x(x):
    current_number = 11
    while current_number <= x:
        if x % current_number == 0:
            return "YES"
        current_number = current_number * 10 + 1
    
    return "NO"

t = int(input())

for _ in range(t):
    x = int(input())
    result = can_make_x(x)
    print(result)
