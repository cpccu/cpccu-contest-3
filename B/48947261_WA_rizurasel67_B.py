def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    alice_dollars = 0
    bob_dollars = 0
    alice_turn = True

    while '0' in s:
        if alice_turn:
            index = s.find('0')
            s = s[:index] + '1' + s[index+1:]
            alice_dollars += 1
        else:
            if is_palindrome(s):
                index = s.find('0')
                s = s[:index] + '1' + s[index+1:]
                alice_dollars += 1
            else:
                s = s[::-1]
                bob_dollars += 1

        alice_turn = not alice_turn

    if alice_dollars < bob_dollars:
        print("ALICE")
    elif alice_dollars > bob_dollars:
        print("BOB")
    else:
        print("DRAW")
