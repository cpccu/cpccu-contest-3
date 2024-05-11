def min_moves_to_win(s):
    n = len(s)
    alice_moves = 0
    bob_moves = 0
    alice_turn = True

    while '0' in s:
        if s == '1' * n:
            # If all characters are '1', it's a draw
            return 'DRAW'

        if alice_turn:
            # Find the leftmost '0' and change it to '1'
            index = s.index('0')
            s = s[:index] + '1' + s[index+1:]
            alice_moves += 1
        else:
            # Reverse the string
            s = s[::-1]
            bob_moves += 1

        alice_turn = not alice_turn

    if alice_moves < bob_moves:
        return 'ALICE'
    elif alice_moves > bob_moves:
        return 'BOB'
    else:
        return 'DRAW'

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(min_moves_to_win(s))
