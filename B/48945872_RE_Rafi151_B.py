def determine_winner(t, test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        s = case[1]

        # Count the number of 'o's in the string
        o_count = s.count('o')

        # If there's only one 'o' left, the next player will win
        if o_count == 1:
            # If the total length is odd, Alice wins
            if n % 2 == 1:
                results.append("ZICE")
            # If the total length is even, Bob wins
            else:
                results.append("30B")
        else:
            # If there's more than one 'o' left, the game will continue and end in a draw
            results.append("DRAW")

    return results

# Input
t = int(input())  # Number of test cases
test_cases = []   # Store test cases
for _ in range(t):
    n = int(input())  # Length of the string
    s = input()       # The string itself
    test_cases.append((n, s))

# Determine the winners
winners = determine_winner(t, test_cases)

# Output
for winner in winners:
    print(winner)
