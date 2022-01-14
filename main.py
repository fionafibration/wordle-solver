import string
from lists import fulllist, wordlist
from random import shuffle
from z3 import *

LETTERS = string.ascii_lowercase
LETTER_FREQ = {'s': 1.0, 'e': 0.999549887471868, 'a': 0.8987246811702926, 'o': 0.6658664666166542, 'r': 0.6238559639909977,
 'i': 0.5639909977494374, 'l': 0.5057764441110277, 't': 0.4943735933983496, 'n': 0.44291072768192047,
 'u': 0.3767441860465116, 'd': 0.36804201050262564, 'y': 0.31117779444861215, 'c': 0.3042760690172543,
 'p': 0.3029257314328582, 'm': 0.2964741185296324, 'h': 0.26406601650412603, 'g': 0.2466616654163541,
 'b': 0.24411102775693924, 'k': 0.22580645161290322, 'f': 0.16729182295573894, 'w': 0.15588897224306075,
 'v': 0.10412603150787697, 'z': 0.06511627906976744, 'j': 0.043660915228807204, 'x': 0.04321080270067517,
 'q': 0.016804201050262566}

letter_to_index_map = {letter: index for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}
index_to_letter_map = {index: letter for letter, index in letter_to_index_map.items()}

word_ = [Int(f"letter_{index}") for index in range(5)]


def model_print(model):
    w = []
    for i, letter_ in enumerate(word_):
        w.append(index_to_letter_map[model[letter_].as_long()])
    return ''.join(w)


def get_solver():
    solver = Solver()

    for letter_var in word_:
        solver.add(letter_var >= 0, letter_var <= 25)

    words_term = []

    for word in wordlist:
        word_term = And([word_[index] == letter_to_index_map[letter] for index, letter in enumerate(word)])
        words_term.append(word_term)

    solver.add(Or(words_term))

    return solver


def correct(l, idx):
    return word_[idx] == letter_to_index_map[l]


def contains(l, idx):
    return And(Or([letter == letter_to_index_map[l] for letter in word_]),
               word_[idx] != letter_to_index_map[l])


def not_contains(l):
    return And([letter != letter_to_index_map[l] for letter in word_])


def not_in_position(l, idx):
    return word_[idx] != letter_to_index_map[l]


# If a letter is green somewhere and then shows up black later, run this on the same spot
def only_correct(l, idx):
    term = []
    for i in range(5):
        if i != idx:
            term.append(word_[i] != letter_to_index_map[l])
    return And(term)


def guess(g):
    return Or([letter != letter_to_index_map[g[i]] for i, letter in enumerate(word_)])


if __name__ == '__main__':
    s = get_solver()
    for l in '':
        s.add(not_contains(l))

    print("Solving...")

    candidates = []

    while s.check() == sat:
        candidate = model_print(s.model())
        candidates.append(candidate)
        s.add(guess(candidate))

    shuffle(candidates)
    print('Possible words: %s' % len(candidates))
    print('First 10: %s' % ' '.join(candidates[:10]))
