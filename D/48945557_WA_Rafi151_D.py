def can_make_number(z):
    # Check if z is divisible by 11
    if z % 11 == 0:
        return "YES"
    else:
        # Check if z can be made by summing up some number of 111s and 11s
        remainder = z % 111
        if remainder == 0 or remainder % 11 == 0:
            return "YES"
        else:
            return "NO"

# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    z = int(input())  # Number to make

    # Check if the number can be made and print the result
    print(can_make_number(z))
