def is_palindrome(s):
    return s == s[::-1]

def who_wins(n, s):
    moves = 0
    while '0' in s:
        if is_palindrome(s):
            idx = s.index('0')
            s = s[:idx] + '1' + s[idx + 1:]
            moves += 1
        else:
            s = s[::-1]
        if is_palindrome(s):
            return moves % 2 == 0, moves % 2 != 0
    return False, False

# Read the number of test cases
t = int(input().strip())

# Iterate through each test case
for _ in range(t):
    # Read input for each test case
    n = int(input().strip())
    s = input().strip()

    # Determine the winner for the current test case
    alice_wins, bob_wins = who_wins(n, s)

    # Output the result for the current test case
    if alice_wins:
        print("ALICE")
    elif bob_wins:
        print("BOB")
    else:
        print("DRAW")
