from immdict import ImmDict
from functools import *


def empty_suffix():
    return ImmDict()


def add_word(suffix, word):
    if suffix.get(word) is None:
        return suffix.put(word, 1)
    else:
        old_pair = suffix.get(word)
        return suffix.put(old_pair[0], old_pair[1] + 1)


# todo: finish and test this
def choose_word(chain, prefix, randomizer):
    suffixes = chain.get(prefix)
    values = suffixes.values()
    sum = reduce(lambda x, y: x + y, values)
    n = randomizer(sum)

    def x(current, pair):
        """pass it the current total, current selected word, and the next pair, increment the total by the pairs
        value, determine whether the n is in the new range and set the word to the word in the pair if it is"""
        total = current[0]
        word = current[1]
        new_word = pair[0]
        new_word_freq = pair[1]
        if word is not "":
            return current
        else:
            if n in range(total, total + new_word_freq):
                return 0, new_word
            else:
                return total + new_word_freq, ""

    reduce(x, zip(chain.keys(), chain.values()), (1, ""))

"""
suffix
builder
generator
"""