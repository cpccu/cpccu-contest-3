def is_palindrome(s):
    return s == s[::-1]

def find_winner(n, s):
    dollars_alice = 0
    dollars_bob = 0

    # Simulate the game
    while '0' in s:
        if s.count('0') == 1:
            # Only one '0' left, Alice will make the last move
            if dollars_alice <= dollars_bob:
                return "ALICE"
            else:
                return "BOB"
        else:
            if s[0] == '0' and s[-1] == '0':
                # Both ends have '0', choose the one with less cost
                if dollars_alice <= dollars_bob:
                    s = '1' + s[1:-1] + '1'
                    dollars_alice += 1
                else:
                    s = '1' + s[1:-1] + '1'
                    dollars_bob += 1
            elif s[0] == '0':
                # Choose the leftmost '0'
                s = '1' + s[1:]
                dollars_alice += 1
            elif s[-1] == '0':
                # Choose the rightmost '0'
                s = s[:-1] + '1'
                dollars_bob += 1
            else:
                # The remaining case is when both ends are '1'
                # If the remaining string is still a palindrome, reverse it
                if is_palindrome(s[1:]):
                    s = s[::-1]
                    if dollars_alice <= dollars_bob:
                        dollars_alice += 1
                    else:
                        dollars_bob += 1
                else:
                    # If the remaining string is not a palindrome, reverse it with minimum cost
                    if dollars_alice < dollars_bob:
                        s = s[::-1]
                        dollars_alice += 1
                    else:
                        s = s[::-1]
                        dollars_bob += 1

    # After the game ends, determine the winner
    if dollars_alice < dollars_bob:
        return "ALICE"
    elif dollars_alice > dollars_bob:
        return "BOB"
    else:
        return "DRAW"

# Read input
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    result = find_winner(n, s)
    print(result)
