def is_palindrome(s):
    return s == s[::-1]

def find_winner(n, s):
    dollars_alice = 0
    dollars_bob = 0
    while '0' in s:
        if s.count('0') == 1:  # If there is only one '0' left
            if dollars_alice < dollars_bob:
                return "ALICE"
            elif dollars_bob < dollars_alice:
                return "BOB"
            else:
                return "DRAW"
        if s[0] == '0':
            if s[-1] == '0':
                if dollars_alice <= dollars_bob:
                    s = s[::-1]
                    dollars_alice += 1
                else:
                    return "BOB"
            else:
                s = s[:-1] + '1'
                dollars_alice += 1
        else:
            if s[-1] == '0':
                s = s[1:] + '1'
                dollars_bob += 1
            else:
                s = s[1:-1] + '1'
                dollars_bob += 1
    return "DRAW"

# Read input
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    result = find_winner(n, s)
    print(result)
