def can_make_x(x):
    # List of numbers: 11, 111, 1111, ...
    numbers = [1]
    while numbers[-1] <= x:
        numbers.append(numbers[-1] * 10 + 1)

    # Iterate through the numbers in reverse order
    for num in reversed(numbers):
        # Check if x can be divided evenly by the current number
        if x % num == 0:
            return "YES"
    return "NO"

# Input
t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    # Output
    print(can_make_x(x))
