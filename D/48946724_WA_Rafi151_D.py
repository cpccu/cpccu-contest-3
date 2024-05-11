def can_make_x(x):
    current = 0
    i = 1
    while current < x:
        current += int('1' * i)
        if current == x:
            return "YES"
        i += 1
    return "NO"

# Input
t = int(input())
for _ in range(t):
    x = int(input())
    print(can_make_x(x))
