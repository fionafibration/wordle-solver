# Contains guess simulation and interpretation
import collections
import string
from colorama import Fore, Back, Style

idict = lambda: collections.defaultdict(int)

LETTERS = string.ascii_lowercase


def correct(l, idx):
    return lambda w: w[idx] == l


def contains(l, idx):
    return lambda w: (w[idx] != l and l in w)


# does not contain
def not_contains(l):
    return lambda w: l not in w


# not in position
def not_in_position(l, idx):
    return lambda w: w[idx] != l


def count(l):
    return lambda w: w.count(l) >= 1


def guess_to_constraints(guess, response):
    letter_count = idict()
    for letter in LETTERS:
        for x in response:
            pass


def print_guess(solution, guess):
    letters_count = {l: solution.count(l) for l in solution}
    colours = {}

    for idx, guess_letter in enumerate(guess):
        if solution[idx] == guess_letter:
            colours[idx] = 'g'
            letters_count[guess_letter] -= 1

    for idx, guess_letter in enumerate(guess):
        if solution[idx] != guess_letter:
            if guess_letter in solution and letters_count[guess_letter]:
                colours[idx] = 'y'
            else:
                colours[idx] = 'b'

    for i in range(5):
        if colours[i] == 'g':
            print(f'{Fore.GREEN}{guess[i]}', end='')
        elif colours[i] == 'y':
            print(f'{Fore.YELLOW}{guess[i]}', end='')
        else:
            print(f'{Fore.RESET}{guess[i]}', end='')


def constrain_guess(solution, guess):
    predicates = []

    for idx, guess_letter in enumerate(guess):



print_guess('artsy', 'attic')
