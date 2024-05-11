t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    # Count the number of '0's
    zeros = s.count('0')

    # Determine the winner based on the number of '0's
    if zeros == 1:
        print("ALICE")
    elif zeros % 2 == 0:
        print("BOB")
    else:
        print("ALICE")
