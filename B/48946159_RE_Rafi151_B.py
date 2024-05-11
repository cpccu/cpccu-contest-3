def is_palindrome(s):
    return s == s[::-1]

def count_zeros(s):
    return s.count('0')

def calculate_winner(n, s):
    # Initial number of zeros in the string
    zeros = count_zeros(s)
    
    # If there's only one zero left, Alice wins
    if zeros == 1:
        return "ALICE"
    
    # If the number of zeros is odd, Bob wins
    if zeros % 2 == 1:
        return "BOB"
    
    # If the number of zeros is even, it's a draw
    return "DRAW"

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    # Calculate the winner for the current test case
    winner = calculate_winner(n, s)
    print(winner)
