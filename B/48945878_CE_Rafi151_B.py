To solve this problem, we need to determine who will win the game based on the given strings. The rules seem to be that if there are an odd number of '1's in the string, Bob wins; if there are an even number of '1's, Alice wins. Since the string is a palindrome, we only need to check one half of the string to count the number of '1's.

Here's a Python solution for this problem:

```python
t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the string
    s = input()  # The string itself
    
    # Count the number of '1's in the first half of the string
    ones_count = s[:n//2].count('1')
    
    # Determine the winner based on the count of '1's
    if ones_count % 2 == 0:
        print("ZICE")  # Alice wins
    else:
        print("30B")  # Bob wins
```

This code reads the input, counts the number of '1's in the first half of each string, and determines the winner based on whether the count is even or odd. Then, it prints the result accordingly.