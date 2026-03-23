def compare(game, guess):
    results = []
    for i in range(len(game)):
        score = 0
        if game[i] == guess:
            score = 0
        results.append(abs(score - game[i]))
    return results