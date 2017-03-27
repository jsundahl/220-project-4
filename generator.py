import prefix
import suffix
from functools import *


def get_word_list(chain, p, randomizer_fn, num_words, NONWORD):
    """start with prefix as ('\n', '\n') then do choose_word with the prefix, return (prefix, word, n-1)"""
    def add_to_word_list(trio_list, x):
        prev_trio = trio_list[-1]
        prev_prefix = prev_trio[0]
        prev_n = prev_trio[2]

        if prev_n <= 0:
            return trio_list
        else:
            new_word = suffix.choose_word(chain, prev_prefix, randomizer_fn)
            new_prefix = prefix.shift_in(prev_prefix, new_word)
            if new_word == NONWORD:
                return trio_list + [(new_prefix, "", 0)]
            else:
                return trio_list + [(new_prefix, new_word, prev_n - 1)]

    trios = list(reduce(add_to_word_list, range(0, num_words), [(p, "", num_words)]))
    return tuple(map(lambda x: x[1], trios[1:]))


def generate(chain, randomizer_fn, num_words, NONWORD):
    return ' '.join(get_word_list(chain, (NONWORD, NONWORD), randomizer_fn, num_words, NONWORD))

