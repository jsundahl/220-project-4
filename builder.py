import suffix
from functools import *
from immdict import ImmDict
NONWORD = '/n'


def line_gen(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line


def pairs_gen(file_name, line_gen_fn):
    def pairs_from_line(words):
        for i in range(0, len(words) - 2):
            yield (words[i], words[i+1]), words[i+2]
    line_gen = line_gen_fn(file_name)
    word_array = line_gen.next().split(' ')
    yield (NONWORD, NONWORD), word_array[0]
    pairs_from_line(word_array[1:])
    for line in line_gen:
        words = line.split(' ')
        pairs_from_line(words)


def add_to_chain(chain, pair):
    if chain.get(pair[0]) is None:
        return chain.put(pair[0], suffix.add_word({}, pair[1]))
    else:
        value = chain.get(pair[0])
        return chain.put(pair[0], suffix.add_word(value, pair[1]))


def build_chain(add_fn, pair_gen, immdict_obj):
    return reduce(lambda d, p: add_fn(d, p), pair_gen, immdict_obj)


def build(file_name):
    gen = pairs_gen(file_name, line_gen)
    return build_chain(add_to_chain, gen, ImmDict())
