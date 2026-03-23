def compare(game, guess):
    results = []
    for i in range(len(game)):
        score = game[i]
        guess = guess[i]
        if score == guess:
            results.append(0)
        else:
            results.append(abs(score - guess))
    return results