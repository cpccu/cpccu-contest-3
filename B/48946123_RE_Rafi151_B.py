def who_wins(n, s):
    if s.count('0') == 1:
        return "BOB"
    elif s.count('0') % 2 == 0:
        return "DRAW"
    else:
        return "ALICE"

# Input reading
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    print(who_wins(n, s))
