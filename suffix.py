from functools import *

from immdict import ImmDict


def empty_suffix():
    return ImmDict()


def add_word(suffix, word):
    if suffix.get(word) is None:
        return suffix.put(word, 1)
    else:
        old_word_freq = suffix.get(word)
        return suffix.put(word, old_word_freq + 1)


# todo: finish and test this
def choose_word(chain, prefix, randomizer):
    suffixes = chain.get(prefix)
    values = suffixes.values()
    sum = reduce(lambda x, y: x + y, values)
    n = randomizer(sum)

    def val_in_range(sum_word, word_pair):
        sum = sum_word[0]
        old_word = sum_word[1]
        if old_word is not None:
            return sum_word
        else:
            word = word_pair[0]
            word_freq = word_pair[1]
            if n in range(sum, sum + word_freq):
                return sum + word_freq, word
            else:
                return sum + word_freq, None
    return reduce(val_in_range, suffixes.get_dict().items(), (1, None))[1]
