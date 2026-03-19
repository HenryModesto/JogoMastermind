def calculate_feedback(secret, guess):
    black = sum(s == g for s, g in zip(secret, guess))

    secret_remaining = []
    guess_remaining = []

    for s, g in zip(secret, guess):
        if s != g:
            secret_remaining.append(s)
            guess_remaining.append(g)

    white = 0
    for g in guess_remaining:
        if g in secret_remaining:
            white += 1
            secret_remaining.remove(g)

    return black, white