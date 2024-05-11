def can_make_x(x):
    numbers = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111]
    for num in reversed(numbers):
        while x >= num:
            x -= num
    return x == 0

# Input
t = int(input())
for _ in range(t):
    x = int(input())
    # Output
    if can_make_x(x):
        print("YES")
    else:
        print("NO")
