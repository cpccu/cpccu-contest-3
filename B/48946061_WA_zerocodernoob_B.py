def play_game(n, s):
    alice_dollars = 0
    bob_dollars = 0
    i, j = 0, n - 1
    last_operation_was_reverse = False

    while i <= j:
        if s[i] == '0':
            if i == j:
                alice_dollars += 1
            else:
                s[i] = '1'

        if s[j] == '0':
            if i != j:
                s[j] = '1'

        if not last_operation_was_reverse and s[i] == '0' and s[j] == '0':
            bob_dollars += 1
            last_operation_was_reverse = True
        else:
            last_operation_was_reverse = False

        i += 1
        j -= 1

    if alice_dollars < bob_dollars:
        return "ALICE"
    elif alice_dollars > bob_dollars:
        return "BOB"
    else:
        return "DRAW"

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s_input = list(input().strip())

        result = play_game(n, s_input.copy())  # Use a copy to avoid modifying the original string
        print(result)
