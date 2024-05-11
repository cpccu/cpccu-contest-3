# Function to determine the winner for each test case
def determine_winner(n, s):
    num_ones = s.count('1')
    if num_ones == 1:
        return "DRAW"
    elif num_ones % 2 == 0:
        return "BOB"
    else:
        return "ALICE"

# Reading the number of test cases
t = int(input())

# Iterating through each test case
for _ in range(t):
    # Reading input for each test case
    n = int(input())
    s = input().strip()
    
    # Determining the winner and printing the result
    print(determine_winner(n, s))
