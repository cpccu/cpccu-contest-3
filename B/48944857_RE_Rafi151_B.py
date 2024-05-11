def is_palindrome(s):
    return s == s[::-1]

def get_winner(n, s):
    dollars_alice = 0
    dollars_bob = 0
    alice_turn = True
    while '0' in s:
        if alice_turn:
            # Alice's turn
            if s[0] == '0':
                s = '1' + s[1:]
                dollars_alice += 1
            else:
                # If the string is not a palindrome, Alice can reverse it
                if not is_palindrome(s):
                    s = s[::-1]
                    dollars_alice += 0
                else:
                    # If the string is already a palindrome, Alice can only flip the first '0'
                    s = '1' + s[1:]
                    dollars_alice += 1
            alice_turn = False
        else:
            # Bob's turn
            if s[-1] == '0':
                s = s[:-1] + '1'
                dollars_bob += 1
            else:
                # If the string is not a palindrome, Bob can reverse it
                if not is_palindrome(s):
                    s = s[::-1]
                    dollars_bob += 0
                else:
                    # If the string is already a palindrome, Bob can only flip the last '0'
                    s = s[:-1] + '1'
                    dollars_bob += 1
            alice_turn = True
    if dollars_alice < dollars_bob:
        return "ALICE"
    elif dollars_bob < dollars_alice:
        return "BOB"
    else:
        return "DRAW"

# Read input
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    result = get_winner(n, s)
    print(result)
