def is_palindrome(s):
    return s == s[::-1]

def play_game(n, s):
    alice_dollars = 0
    bob_dollars = 0
    last_operation = None
    
    while '0' in s:
        if is_palindrome(s):
            i = s.find('0')
            s = s[:i] + '1' + s[i+1:]
            alice_dollars += 1
            last_operation = 'change'
        else:
            s = s[::-1]
            last_operation = 'reverse'
        
        if '0' not in s:
            break
        
        if is_palindrome(s):
            i = s.find('0')
            s = s[:i] + '1' + s[i+1:]
            bob_dollars += 1
            last_operation = 'change'
        else:
            s = s[::-1]
            last_operation = 'reverse'
    
    if alice_dollars < bob_dollars:
        return "Alice wins"
    elif alice_dollars > bob_dollars:
        return "Bob wins"
    else:
        return "Draw"

# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the input n and the string s for each test case
    n = int(input())
    s = input().strip()
    # Play the game and print the result
    print(play_game(n, s))
