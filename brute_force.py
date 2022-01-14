from lists import *
import tqdm



def simulate_guess(target, guess):
    p = []
    already_correct = []
    already_contained = []
    for l, idx in enumerate(guess):
        # green
        if target[idx] == l:
            p.append(correct(l, idx))
            already_correct.append(l)

        # yellow
        elif l in target:
            if l in already_correct and target.count(l) == 1:

            p.append(contains(l, idx))
            already_contained.append(l)

    for i, gletter in enumerate(guess):
        if target[i] == gletter:
            p.append(correct(gletter, i))
        elif gletter in target:
            p.append(contains(gletter, i))
        else:
            p.append(not_contains(gletter))
    return p


def get_best(candidates, current_predicates):
    if predicates is None:
        predicates = []
    if possible is None:
        possible = wordlist

    guess_ratings = defaultdict(list)

    if len(possible) == 1:
        return possible[0]

    for candidate in tqdm(possible):
        for guess in wordlist:
            if candidate == guess:
                continue
            before = 2315
            new_predicates = simulate_guess(candidate, guess)

            after = len(get_possible(new_predicates, possible))

            guess_ratings[guess].append(before / after)

    guess_avg = {}

    for word, scores in guess_ratings.items():
        guess_avg[word] = sum(scores) / len(scores)

    bestguesses = {k: v for k, v in sorted(guess_avg.items(), key=lambda item: item[1])}

    return bestguesses[0]


get_best()
