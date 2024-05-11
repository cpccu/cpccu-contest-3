def winner_of_game(s):
    count_ones = s.count('1')
    if count_ones % 2 == 0:
        if count_ones == 1:
            return "DRAW"
        else:
            return "BOB"
    else:
        return "ALICE"

# Read input
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    result = winner_of_game(s)
    print(result)
